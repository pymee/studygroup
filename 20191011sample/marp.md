---
marp: true
---

<!-- $theme: gaia -->
<!-- page_number: true -->
<!-- paginate: true -->

# Pymee2019 第1回勉強会サンプルプログラム

---

# はじめに
このプログラムは Pymee2019 第 1 回勉強会のサンプルプログラムです。    
  
2018 年の勉強会で学んだことを使って作っています。  
一部変なところもあるかもしれないですが、動いてるので今回はよし。

---

# venv
以下のコマンドを実行すると開発者と同じライブラリの環境で試せます。

```sh
source venv/bin/activate
pip install -r requirements.txt
```
* venvがなにか知りたい人はGoogle先生に聞いてください。

---

## コードの解説

ここからはコードと何をやっているのかを簡単に書いていきます。

---

## ライブラリのインポート

```python
#!/user/bin/env python3

import csv
import os
import string
import sys
from datetime import datetime

import paramiko

```

※1行目はShebangです。詳細はGoogle先生に聞いてください。

---

## 引数のチェック

```python
# コマンドライン引数の数のチェック
if len(sys.argv) <= 1:
    print("Usage: {} <csvfile>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
```

* 今回は引数が1以下のときに`sys.exit(1)`で終了させています。

---

## IPアドレスの記載されたCSVのチェック

```python
# コマンドライン引数で指定したcsvファイルがなければ終了させる
if not os.path.exists(sys.argv[1]):
    print("ERROR: CSVファイルが見つかりません")
    sys.exit(1)
elif os.path.getsize(sys.argv[1]) <= 10:
    print("ERROR: ファイルが空の可能性があります。")
    sys.exit(1)
```

*  `elif os.path.getsize(sys.argv[1]) <= 10:`の部分はファイルが空かどうかの判定で使っています。  
* 他にもいい方法があると思いますが、IP アドレスだけで 10 文字は行くと思ったのでこの書き方してみました。

---

## paramikoの初期設定

```python
# Paramikoをインスタンス化して初期設定とか済ませておく
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```

* paramiko モジュールをインスタンス化してから各種設定しています。 


---

## stringモジュールでテンプレート作成
```python
# 出力用のテンプレートを生成
templates_text = string.Template("""\
====================
IPアドレス: $ipaddr
ログインユーザ: $username
実行時刻: $nowtime
====================
# $command
$command_result

""")
```

* 出力用のテンプレートを定義しています。

---

## CSVモジュールを使って色々する

```python
# CSVファイルを開いてIPアドレス、ユーザ名、パスワード、コマンドを取り出したあとにコマンドを実行して出力テキストを生成
with open(sys.argv[1], 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if not row[0] == "":
            hostname = row[0]
            username = row[1]
            password = row[2]
        command = row[3]
```

* CSVファイルを開いてIPアドレス、ユーザ名等を取り出して変数に代入しています。

---

## サーバに接続
```python
        # サーバに接続
        try:
            ssh.connect(hostname=hostname, username=username, password=password,
                        port=22, timeout=15.0, look_for_keys=False)
        except paramiko.ssh_exception.AuthenticationException as e:
            print("ERROR: SSH接続に失敗しました。", file=sys.stderr)
            sys.exit(1)
```

* ユーザ名やパスワード違いで認証に失敗した場合には`except`の部分が処理される。

---

## コマンドの発行と出力テキストの作成

```python
        # コマンド発行
        stdin, stdout, stderr = ssh.exec_command(command)

        command_result = ""

        # 標準出力のリストをリスト内包表記で作る
        for i in stdout:
            command_result += i.strip('\n') + '\n'

        contents += templates_text.substitute(ipaddr=hostname, username=username,
                                              nowtime=datetime.now().strftime("%H:%M"),
                                              command=command, command_result=command_result)
```

* コマンドの実行結果をテンプレートに反映させてからcontents変数に代入しています。

---

## 保存ファイル名の生成とフォルダのチェック

```python
# 保存場所の定義（全角にしたのは定数として認識しやすくするためで、Pythonでは特に意味は持たない）
SAVE_FILE_PATH = "./results/"
SAVE_FILE_NAME = "out_{}.txt".format(datetime.now().strftime("%Y%m%d%H%M"))

SAVE_PATH = SAVE_FILE_PATH + SAVE_FILE_NAME

# resultsフォルダがあるかチェックしてなければ作成
if not os.path.exists(SAVE_FILE_PATH):
    os.mkdir(SAVE_FILE_PATH)
```

* 大文字の変数は定数的な意味で大文字にしてありますが、Pythonに定数はないので特にプログラム的な意味はありません。

---

## 保存処理

```python

# 同じファイル名があるかチェックしてから保存処理
try:
    if os.path.isfile(SAVE_PATH):
        raise FileExistsError()
    with open(SAVE_PATH, 'a', encoding='UTF-8') as f:
        f.write(contents)

    print("保存完了！")
except FileExistsError:
    print("ファイル名 [{}] は重複しています。".format(SAVE_FILE_NAME), file=sys.stderr)
    sys.exit(1)
```

* `FileExistsError`で保存ファイル名が重複する場合には例外処理をしてます。
