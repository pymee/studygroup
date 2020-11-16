
# pymee勉強会

---

<!-- page_number: true -->

# 事前準備
以下の3点が完了していることの確認をお願いします

* pythonのインストール
* メーラーのインストール
* 勉強会資料のダウンロード

本日の勉強会はzoomで録画し、eschoolで公開予定です。

---

# 勉強会について

* 目的
プログラムに興味を持ってもらう
身近な業務である<b>メール作成業務の自動化</b>をテーマに！
* スケジュール
	- 12/4 勉強会＆課題の提示
	- 各自課題対応(2ヶ月)
	- 2/X 課題の発表@zoom

* tocaroのチャットで思ったことや疑問点をどんどん投稿してください
* 「へー」とか、「ふーん」とかでもOKです笑

---

# メール作成業務の自動化について①
株式会社pymeeのサービスを運用しています
サービスメンテナンスをユーザに通知することになりました

csvファイルに記載されている100人のユーザへメール通知を行う必要があります

ユーザ通知まで時間があるので、事前にメール(emlファイル)を作成しようと思いました

---

# メール作成業務の自動化について②
* csvファイル
宛先メールアドレス、CCのアドレス、ユーザの会社名、宛名でデータが並んでいます

[todo]csvファイルの画像を貼る

* メールフォーマット
メールフォーマットの画像を貼る

---

# 実際にプログラムでメールを作成してみると・・・

* 実際にプログラムを実行してメールを作成してみます！

---

# 実際にプログラムでメールを作成してみると・・・

* 実際にプログラムを実行してメールを作成してみます！
</br>

<b>難しそう・・・と思ったかもしれませんが、今日の勉強会でできるようになります！！</b>

---

# アジェンダ
* プログラムって何？
* 自動化する前に業務の自動化を考えてみる
* 1通のメールを作成するプログラムを実行してみる
* `1通のメールを作成するプログラムを修正してみる`
* `csvファイルからデータを読み込む`
* `自分で作ってみる`
* 今後の流れについて

灰色部分が実際にコードを修正/作成してもらう部分になります
 
---

# プログラムって何？
* コンピュータにやってもらいたい処理を書いて指示すること
* 指示内容について書いたものが「プログラム」！！
	* プログラムを実行するには「実行環境」が必要
	* 一般的にプログラムを書くことをプログラミングという

[todo] 画像を貼る

---

# プログラムも万能ではない・・・
* プログラムは指示書
	* 手順、明確な判断基準がないとプログラムは想定通りにはならない
	* プログラムは繰り返し処理が得意

[todo] 画像を貼る

---

# プログラムを書く前に(5分)
* 今日自動化する業務の手順を考えてみよう！
	* メール作成業務の自動化について①、②の内容を読んで、手順を考えてみてください
	* 考えた結果をtocaroのチャットに投稿してみてください〜

---

# 手順例

1. csvファイルを開く
1. メールを新規作成する
1. csvファイルの宛先をコピーしてメールの宛先に貼り付ける
1. csvファイルのCCをコピーしてメールの宛先に貼り付ける
1. 件名を入力する
1. 本文をコピーして貼り付ける
1. csvファイルの会社名をコピーし本文の<会社名>の部分に貼り付ける
1. csvファイルの宛名をコピーし本文の<宛名>の部分に貼り付ける
1. サービスメンテナンスのご連絡_<会社名>_<宛名>.emlの名前で保存する
1. csvの終わりまで繰り返す

---

# 手順
部分的にプログラムを作っていこうと思います！

1. 1通のメールを作成するプログラムを実行してみる
2. 1通のメールを作成するプログラムを修正する
3. csvファイルデータを取り出してみる
4. csvファイルのデータを取り出し、メールを作成する

---

# 1通のメールを作成するプログラムを実行してみる(5分)

1. メールが格納されるフォルダ「result」を「mail_create1_example.py」と同じ階層に作成
2. 以下どちらかの方法でプログラムを実行します

    * Windowsの実行方法
      ```
      $ py mail_create_1_example.py
      ```
    * Mac/Linuxの実行方法
      ```
      $ python3 mail_create_1_example.py
      ```
		Mac/Linuxでは「python mail_create_1_example.py」でも実行できますが、python2で実行される可能性がるため上記方法での実行をお願いします。

---

# 1通のメールを作成するプログラムを実行してみる(5分)
3. 結果を確認する
    * コンソールに以下が出力。**※本文は読めない形式で出力**
      ![50%](../image/1_example_result1.png)
    * 「result」フォルダにメールが作成されること
      ![65%](../image/1_example_result2.png)

---

# プログラムの中身をみてみよう
その前に、メールのデータについておさらいです！

* メールデータのフォーマットはヘッダ部とボディ部に分かれています
    * ヘッダ部のフォーマットは以下の通りです
	  * To:には宛先メールアドレス
	  * From；に送信元メールアドレス
	  * CC:にCCのメールアドレス
	  * Subject:には件名
    * ボディ部には本文が記載されています

[TODO]画像を貼る

---

# プログラムの中身をみてみよう
* テキストエディタで以下のファイルを開いてみてください
  * ファイル名:mail_create_1_example.py

---

# プログラムの中身をみてみよう
1. メール作成の機能をもつモジュールの呼び出し
<font style = "font-size:70%">
    ```python
    from email.message import EmailMessage
    from email.generator import Generator
    ```
</font>

2. ファイルに書き込むためのメールデータの準備
<font style = "font-size:70%">
    ```python
    # <会社名>と<宛名>の部分を関数で書き換えてみよう
    message = """<会社名>　<宛名>様

    お世話になっております。pymeeです。
    (中略)

    # 本文を設定する
    mail_data.set_content(message)
    ```
</font>

3. ファイルへの書き込み
<font style = "font-size:65%">
    ```python
    # 設定した内容をファイルに書き込む
    with open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',
    company).replace('<宛名>',name), 'w') as eml:
        eml_file = Generator(eml)
        eml_file.flatten(mail_data)
    ```
</font>

---

# プログラムの中身をみてみよう(モジュールについて)

<font style = "font-size:70%">
  
```python
from email.message import EmailMessage
from email.generator import Generator
```
</font>

pythonでメールデータを扱うためのモジュール(プログラム)を呼び出しています。

* email.messageの中のEmailMessageモジュールを呼び出し
* email.generatorの中のGeneratorモジュールを呼び出し

呼び出さないとこれらの機能は使用できません。
また、これらはすでにインストール済みのため、追加インストールは不要です。


---

# プログラムの中身をみてみよう(変数について)

<font style = "font-size:70%">
  
```python
# 変数の設定
# 送信元、宛先、CCのメールアドレス、会社名、宛名を変数で定義してメールを作成してみよう！
subject = 'サービスメンテナンスのご連絡'
company = '株式会社A'
name = '佐藤'
```
</font>

* 変数とは？
変数は、ラベルがついた箱のようなものです。
変数にデータを代入することができます。

* 変数の宣言
一度変数を宣言すれば、それ以降は変数を指定することでデータを扱うことができます。

* データ型
文字列は「'」もしくは「"」で文字列を囲む必要があります。

---

# プログラムの中身をみてみよう(変数について)
* 文字列の中に改行があり複数行ある場合は、"""で囲むやり方があります
    <font style = "font-size:70%">
    ```python
    # <会社名>と<宛名>の部分を関数で書き換えてみよう
    message = """<会社名>　<宛名>様

    お世話になっております。pymeeです。

    いつも【サービスA】をご利用いただきありがとうございます。
    以下日程にてサービスメンテナンスを実施いたします。

    2020年12月30日 23:00 〜 12月31日 6:00

    ご迷惑をおかけしますが、
    メンテナンス時間は弊社サービスをご利用いただけませんので、
    ご了承くださいませ。

    以上です。よろしくお願いいたします。
    """
    ```
    </font>

---

# プログラムの中身をみてみよう(メールデータの作成)
<font style = "font-size:70%">

```python
# メールを作成する
mail_data = EmailMessage()

# 送信元アドレスを設定する
mail_data['From'] = '送信元メールアドレス'

# 宛先アドレスを設定する
mail_data['To'] = '宛先メールアドレス'

# CCアドレスを設定する
mail_data['CC'] = 'CCのメールアドレス'

# 件名を設定する
mail_data['subject'] = subject

# 本文を設定する
mail_data.set_content(message)
```
</font>

先ほど宣言した変数subject、messageを使用しています。

---

# プログラムの中身をみてみよう(メールデータの表示)
<font style = "font-size:70%">
  
```python
# mail_dataの中身をみてみる
print(mail_data)
```
</font>

* 標準出力(コマンドプロンプト/コンソール)にmail_dataの中身を出力させています
	![80%](../image/1_example_result1.png)

---

# プログラムの中身をみてみよう(メールデータの書き込み)

<font style = "font-size:70%">
  
```python
with open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',
company).replace('<宛名>',name), 'w') as eml:
    eml_file = Generator(eml)
    eml_file.flatten(mail_data)
```
</font>

* openの行で書き込み用のファイルを変数emlとして開いています
* withの範囲内であれば、変数emlを使用してデータを扱うことが可能です
* 以下のような書き方もできますが、close()処理を記載する必要があります。withの場合、close処理も自動で行なってくれるので便利です！

<font style = "font-size:70%">
  
```python
# ファイルオープン
eml = open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',
company).replace('<宛名>',name), 'w')
eml_file = Generator(eml)
eml_file.flatten(mail_data)

# closeを書く必要がある
eml.close()
```
</font>

---

# replace関数について

<font style = "font-size:70%">

```python
`〜ご連絡_<会社名>_<宛名>.eml`.replace('<会社名>',company).replace('<宛名>',name)
```
</font>

* 関数とは？
特定の機能をもつプログラムの塊です。
replace関数とは文字を置き換える機能を持っています。
<会社名>を変数companyに代入されたデータに、<宛名>を変数nameに代入されたデータに置き換えています。

---

# replace関数

```
変換対象の文字列.replace(変換前, 変換後)
```
* ()の中を引数といいます
* 今回のようにreplaceを複数回使用することも可能です
* 置き換える機能を持った他の関数もありますのでぜひ調べてみてください！置き換える機能以外の関数もたくさんあります！！

---

# 手順
部分的にプログラムを作っていこうと思います！

1. ~~1通のメールを作成するプログラムを実行してみる~~
2. 1通のメールを作成するプログラムを修正する
3. csvファイルデータを取り出してみる
4. csvファイルのデータを取り出し、メールを作成する

---

# 2. 1通のメールを作成するプログラムを修正する
* 作成されたメールをみてみると・・・
  * 宛先、送信元、CCのメールアドレスがアドレスでない
  * 本文が<会社名>　<宛名>のまま
    ![95%](../image/1_example_result2.png)

---

# 問題　(10分)

* 宛先、送信元、CCのメールアドレスの変数を定義してメールを作成してみよう！
* replace関数を使用して本文の<会社名>　<宛名>を置換してみよう！

  ```
  送信元メールアドレス：pymee-support@example.com
  宛先メールアドレス：satou@exampleA.co.jp
  CCメールアドレス：pymee-support@example.com
  会社名：株式会社A
  宛名：佐藤
  ```

* **変数名ですがfromは予約語なので使えません・・・**

---

# 回答例 (1/2)
<font style = "font-size:70%">
  
```python
from email.message import EmailMessage
from email.generator import Generator

# 変数の設定
# 送信元、宛先、CCのメールアドレスを変数で定義してメールを作成してみよう！
subject = 'サービスメンテナンスのご連絡'
company = '株式会社A'
name = '佐藤'
from_mail = 'pymee-support@example.com'
to_mail = 'satou@exampleA.co.jp'
cc_mail = 'pymee-support@example.com'

# <会社名>と<宛名>の部分を関数で書き換えてみよう
message = """<会社名>　<宛名>様

お世話になっております。pymeeです。

いつも【サービスA】をご利用いただきありがとうございます。
以下日程にてサービスメンテナンスを実施いたします。

2020年12月30日 23:00 〜 12月31日 6:00

ご迷惑をおかけしますが、
メンテナンス時間は弊社サービスをご利用いただけませんので、
ご了承くださいませ。

以上です。よろしくお願いいたします。
""".replace('<会社名>', company).replace('<宛名>', name)
```

</font>

---

# 回答例 (2/2)
<font style = "font-size:70%">
  
```python
# メールを作成する
mail_data = EmailMessage()

# 送信元アドレスを設定する
mail_data['From'] = from_mail

# 宛先アドレスを設定する
mail_data['To'] = to_mail

# CCアドレスを設定する
mail_data['CC'] = cc_mail

# 件名を設定する
mail_data['subject'] = subject

# 本文を設定する
mail_data.set_content(message)

# mail_dataの中身をみてみる
print(mail_data)

# 設定した内容をファイルに書き込む
with open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',
company).replace('<宛名>',name), 'w') as eml:
    eml_file = Generator(eml)
    eml_file.flatten(mail_data)
```
</font>

---

# 手順
部分的にプログラムを作っていこうと思います！

1. ~~1通のメールを作成するプログラムを実行してみる~~
2. ~~1通のメールを作成するプログラムを修正する~~
3. csvファイルデータを取り出してみる
4. csvファイルのデータを取り出し、メールを作成する

---

# csvファイルを扱うには・・・

* やりたいこと
	* csvファイルの中の,で区切られた値を取り出してプログラムに使いたい
* どうするのか？
	1. csvファイルを開く
	1. csvファイルのデータを読み込む
	1. 読み込んだデータを扱いやすい形にする

---

# 実施にcsvファイルのデータを読み込んで標準出力に表示させてみます

---


# どうやったのか？
csvファイルからデータを取り出し中身を出力するプログラムがあります。
ファイル名：mail_create_2_example.py
<font style = "font-size:70%">
  
```python
import csv

# CSVファイルを開く
with open('../data/address2.csv', 'r') as f:
    # csvファイルのデータを読み込む
    csv_data = csv.reader(f)

    # csv_dataの１行分のデータをlineに格納する
    for line in csv_data:
        # lineを表示させる
        print('lineの中身：{}'.format(line))
#        print('宛先メールアドレス：{}'.format(line[0]))
#        print('CCメールアドレス：{}'.format(line[1]))
        print('------')
```
</font>

---

# 出力結果

<font style = "font-size:70%">
  
```python
% python3 mail_create_2_example.py
lineの中身：['satou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社',
'佐藤', 'A']
------
lineの中身：['sakashita@exampleB.co.jp', 'pymee-support@example.co.jp',
'株式会社B社', '坂下', 'B']
------
lineの中身：['saitou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社',
'斎藤', 'B']
------

```
</font>

---

# openにより読み取り専用でcsvファイルを開く

<font style = "font-size:70%">
  
```python
import csv

with open('data/address2.csv', 'r') as f:
    # csvファイルのデータを読み込む
    csv_data = csv.reader(f)
```
</font>

* csvファイルを扱う機能を持ったモジュールcsvを呼び出し
* withとopenを使ってcsvファイルを開く
* csv.reader()でデータをよ見込み、変数csv_dataに格納

---

# forによる繰り返し処理

<font style = "font-size:70%">
  
```python
    for line in csv_data:
        # lineを表示させる
        print('lineの中身：{}'.format(line))
```
</font>

[TODO] 図をいれる
csvファイルの１行目を取り出し標準出力へ表示
次の行へ移動
csvファイルの１行目を取り出し標準出力へ表示
次の行へ移動
...をcsvファイルの終わりまで繰り返している

---

# 標準出力について

<font style = "font-size:70%">
  
```python
 print('lineの中身：{}'.format(line))
```
</font>

* print関数とは？
	()の中身を標準出力へ表示させる機能を持った関数
* format関数とは？
	文字列.format(変数)と記載することで{}の中に変数を格納したものを表示させることが可能
    
    <font style = "font-size:70%">
  
    ```python
    '1つ目：{},2つ目:{}'.format('test1', 'test2')
    // 1つ目：test1,2つ目:test2 と表示される
    ```
    </font>

---

# 値を1つ取り出すには？

* リストとして扱うことが可能

<font style = "font-size:70%">
  
```python

import csv

# CSVファイルを開く
with open('data/address2.csv', 'r') as f:
    # csvファイルのデータを読み込む
    csv_data = csv.reader(f)

    # csv_dataの１行分のデータをlineに格納する
    for line in csv_data:
        # lineを表示させる
        print('lineの中身：{}'.format(line))
        print('宛先メールアドレス：{}'.format(line[0]))
        print('CCメールアドレス：{}'.format(line[1]))
        print('------')
```
</font>

---

# 出力結果

<font style = "font-size:70%">
  
```python

 % python3 mail_create_2_example.py
lineの中身：['satou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社',
'佐藤', 'A']
宛先メールアドレス：satou@exampleA.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
lineの中身：['sakashita@exampleB.co.jp', 'pymee-support@example.co.jp',
'株式会社B社', '坂下', 'B']
宛先メールアドレス：sakashita@exampleB.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
lineの中身：['saitou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社', 
'斎藤', 'B']
宛先メールアドレス：saitou@exampleA.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
```
</font>

---

# リストって？
* 複数のデータをまとめたもの
* まとめた順番によってデータを取り出すことが可能
	* 1番目のデータを取り出すには[0]と指定する
	* 2番目のデータを取り出すには[1]と指定する・・・ 

[TODO] 図をいれる

---

# リストの追加方法

<font style = "font-size:70%">
  
```python

test1 = 'test1'
test2 = 'test2'
test3 = 'test3'

# リストの定義
list_data = []

# リストへのデータの追加
list_data.append(test1)
list_data.append(test2)
list_data.append(test3)

print(list_data)

# 出力結果
['test1', 'test2', 'test3']

```

</font>

---

# withの範囲外になるとデータの読み込みができない

<font style = "font-size:70%">

```python

import csv

# CSVファイルを開く
with open('data/address2.csv', 'r') as f:
    # csvファイルのデータを読み込む
    csv_data = csv.reader(f)

    # csv_dataの１行分のデータをlineに格納する
    for line in csv_data:
        # lineを表示させる
        print('lineの中身：{}'.format(line))
        print('宛先メールアドレス：{}'.format(line[0]))
        print('CCメールアドレス：{}'.format(line[1]))
        print('------')

# ここでcsv_dataを読み込みができない
for line in csv_data:
    print('lineの中身：{}'.format(line))
    print('------')
```
</font>

---

# 出力結果

<font style = "font-size:70%">
  
```python
% python3 mail_create_2_example.py
lineの中身：['satou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社', 
'佐藤', 'A']
宛先メールアドレス：satou@exampleA.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
lineの中身：['sakashita@exampleB.co.jp', 'pymee-support@example.co.jp', '株式会社B社', 
'坂下', 'B']
宛先メールアドレス：sakashita@exampleB.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
lineの中身：['saitou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社',
'斎藤', 'B']
宛先メールアドレス：saitou@exampleA.co.jp
CCメールアドレス：pymee-support@example.co.jp
------
Traceback (most recent call last):
  File "mail_create_2_example.py", line 17, in <module>
    for line in csv_data:
ValueError: I/O operation on closed file.
(venv) sanoyui@sanonoMacBook-Air pymee % 

```
</font>

---

# 解決策

* withの範囲の中で、データを格納するリスト型の変数を定義し、そこに１行分のデータを追加する

---

# 問題(20分)
* mail_create_2_before.pyに以下のように修正する
	1. csvファイル「data/address2.csv」からデータを取り出し「会社名: <会社名>, 宛名: <宛名>」のフォーマットで出力させてみよう
	1. リスト型のlist_dataにcsvファイルのデータを追加して扱いやすいデータにしてみよう

* 出力結果
<font style = "font-size:70%">
  
```
% python3 mail_create_2_before.py
会社名: 株式会社A社, 宛名: 佐藤
会社名: 株式会社B社, 宛名: 坂下
会社名: 株式会社A社, 宛名: 斎藤
[['satou@exampleA.co.jp', 'pymee-support@example.co.jp', '株式会社A社', '佐藤', 'A'],
['sakashita@exampleB.co.jp', 'pymee-support@example.co.jp', '株式会社B社', '坂下', 
'B'], leA.co.jp', 'pymee-support@example.co.jp', '株式会社A社', '斎藤', 'B']]
```
</font>

---

# 手順
部分的にプログラムを作っていこうと思います！

1. ~~1通のメールを作成するプログラムを実行してみる~~
2. ~~1通のメールを作成するプログラムを修正する~~
3. ~~csvファイルデータを取り出してみる~~
4. csvファイルのデータを取り出し、メールを作成する

---

# csvファイルのデータを取り出し、メールを作成する(30分)

今までのことを参考にcsvファイルのデータを取り出し、メールを作成するプログラムを作ってみよう！

---

# ちょっと物足りないな・・・
* csvファイルの最後の列が本文のパターンを示しています
* 次スライドの条件分岐を参考に、最後の列がAの場合は本文Aを、最後の列がBの場合は本文Bを出力するようにプログラムを修正してみてください！
* 本文Aはdata/messageA.txt、本文Bはdata/messageB.txtになります

---

# 条件分岐について

```python
if 条件A :
	処理A
elif 条件B :
	処理B
else:
	それ以外の処理
```
* 条件について

[TODO]条件の一覧を貼る

---


# プログラムを作ってみてどうでしたか？
* 感想をtocaroのチャットに書き込んでいただけると嬉しいです・・・

---

# アジェンダ
* プログラムって何？
* 自動化する前に業務の自動化を考えてみる
* 1通のメールを作成するプログラムを実行してみる
* `1通のメールを作成するプログラムを修正してみる`
* `csvファイルからデータを読み込む`
* `自分で作ってみる`
* 今後の流れについて

灰色部分が実際に手を動かしてもらう部分になります
 
---

# 課題：プログラムをカスタマイズしてみよう！
* TO,CC,宛名が複数ある場合
* メールをアドレスによってフォルダ分けする
* 件名と本文をテキストファイルから読み込む場合
* 暗号化したファイルを添付し、パスワードを通知するメールも合わせて作成する

* 上記以外でもこんなツールだったら使いやすいのになという機能を追加してもらって構いません！！

---

# 発表について
* 作成したコード
* 以下3点をまとめたスライド(3-4枚程度)
	* コード流れの概要説明
	* 特に頑張ったところ
	* 難しかったところ

* 発表の時間がとることが難しい場合、tocaroに資料をアップするでも問題ないです！
* 質問等は随時tocaroもしくはMLで受け付けます！

---

# アンケートのお願い

---

# 本日はお疲れ様でした！
これを機会にちょっとでもプログラムに興味を持っていただけると幸いです・・・！

---