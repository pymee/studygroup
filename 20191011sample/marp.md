---
marp: true
---

<!-- $theme: gaia -->
<!-- page_number: true -->
<!-- paginate: true -->

# Pymee2019
　　
　　
## 第1回勉強会サンプルプログラム

---

# はじめに
このプログラムは Pymee2019 第 1 回勉強会のサンプルプログラムです。    
  
2018 年の勉強会で学んだこと+αを使って作っています。  
一部変なところもあるかもしれないですが、動いてるので今回はよし。

---

# venv
以下のコマンドを実行すると開発者と同じライブラリの環境で試せます。

```sh
source venv/bin/activate
pip3 install -r requirements.txt
```
* venvがなにか知りたい人はGoogle先生に聞いてください。

---

## コードの解説

ここからはコードと何をやっているのかを簡単に書いていきます。

---

## ライブラリのインポート

```python
import csv
import os
import string
import sys
from datetime import datetime

import paramiko
```

* paramikoモジュールのみpipでインストールした物なので1行開けて書いています。

---

## 引数のチェック

```python
# コマンドライン引数の数のチェック
if len(sys.argv) <= 1:
    print("Usage: {} <csvfile>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

csv_file_path = sys.argv[1]
```

* 今回は引数が1以下のときに`sys.exit(1)`で終了させています。
* `csv_file_path`変数にCSVファイルのパスを代入しています。

---

## IPアドレスの記載されたCSVのチェック

```python
# コマンドライン引数で指定したcsvファイルがなければ終了させる
if not os.path.exists(csv_file_path):
    print("ERROR: CSVファイルが見つかりません")
    sys.exit(1)
elif os.path.getsize(csv_file_path) == 0:
    print("ERROR: ファイルが空の可能性があります。")
    sys.exit(1)
```

*  `elif os.path.getsize(csv_file_path) == 0:`の部分はファイルが空かどうかの判定で使っています。  

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
$command
$command_result

""")
```

* 出力用のテンプレートを定義しています。

---

## CSVモジュールを使って色々する

```python
# CSVファイルを開いてIPアドレス、ユーザ名、パスワード、コマンドを取り出したあとにコマンドを実行して出力テキストを生成
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

   for row in csv_reader:
        if not (row[0] == "" and row[1] == "" or row[0] == "" and row[1] == "" and row[2] == ""):
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
* `AuthenticationException`でSSH接続の認証系ほとんどキャッチできると思います。

---

## ホストネームの取得とプロンプトの生成

```python
# ホスト名を取得 Linuxの $HOSTNAME 環境変数でホスト名を取得
        stdin, stdout, stderr = ssh.exec_command("echo $HOSTNAME")
        server_hostname = stdout.readline().strip("\n")

        # プロンプトの構築
        prompt = "[{user}@{hostname}]".format(user=username, hostname=server_hostname) 
        
        # 三項演算子を使用して一行でif-elseを書く
        prompt += "# " if username == "root" else "$ "
```

* 出力のテキストに使うPROMPTを生成

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
                                              command=prompt+command, command_result=command_result)
        # 念の為コネクションをクローズしておく
        ssh.close()
```

* コマンドの実行結果をテンプレートに反映させてからcontents変数に代入しています。

---

## 保存処理

```python
# 保存ファイル名の定義（全角にしたのは定数として認識しやすくするためで、Pythonでは特に意味は持たない）
SAVE_FILE_NAME = "out_{}.txt".format(datetime.now().strftime("%Y%m%d%H%M"))

# 保存処理
try:
    with open(SAVE_FILE_NAME, 'x', encoding='UTF-8') as f:
        f.write(contents)

    print("保存完了！")
except FileExistsError:
    print("ファイル名 [{}] は重複しています。".format(SAVE_FILE_NAME), file=sys.stderr)
    sys.exit(1)
```

* 大文字の変数は定数的な意味で大文字にしてありますが、Pythonに定数はないので特にプログラム的な意味はありません。