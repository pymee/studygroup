<!-- page_number: true -->

# 第5回 Pymee

---
課題作成に必要となるCSVモジュール、paramikoモジュールの基本的な使い方

# CSVモジュール

pythonでCSVファイルを取り扱うためのモジュールの使用例

---

+ some.csv
```
172.31.23.70,ec2-user,P@ssw0rd!
172.30.30.239,ec2-user,P@ssw0rd!
```
上記のファイルをpythonプログラムから読み込みます。

---
+ csvread.py
```python
#!/usr/bin/python3

import csv

f = open('some.csv', 'r')

reader = csv.reader(f)
for row in reader:
    print("================================================")
    print("行")
    print(row)
   
    print("1列目") 
    print(row[0])
    print("2列目") 
    print(row[1])
    print("3列目") 
    print(row[2])

f.close()
```
CSVファイルをオープンしreaderに格納します。
読み取ったCSVファイルは行ごとに配列として格納されます。
読み取ったファイルの各行と要素を表示させます。

---
+ 出力結果
```
[root@ip-172-31-24-55 ~]# ./csvread.py
================================================
行
['172.31.23.70', 'ec2-user', 'P@ssw0rd!']
1列目
172.31.23.70
2列目
ec2-user
3列目
P@ssw0rd!

================================================
行
['172.30.30.239', 'ec2-user', 'P@ssw0rd!']
1列目
172.30.30.239
2列目
ec2-user
3列目
P@ssw0rd!
```
CSVファイルの行と要素を表示できています。


# paramikoモジュール

pythonでssh接続するためのparamikoモジュールの使用例

---

+ paramikossh.py
```python
#!/usr/bin/python3

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.31.23.70', username='ec2-user', password='P@ssw0rd!')


stdin, stdout, stderr = client.exec_command('hostname')
for line in stdout:
    print(line)

client.close()
```
パスワード認証にてサーバにログインすることを想定しています。
ログイン情報は以下の通りです。
+ ログイン対象：172.31.23.70
+ ユーザ：ec2-user
+ パスワード：P@ssw0rd!

上記サーバにて「hostname」コマンドを実行し結果を表示させます。

---
+ 出力結果
```
[root@ip-172-31-24-55 ~]# ./paramikossh.py 
ip-172-31-23.70.ap-northeast-1.compute.internal
```
ログイン対象である172.31.23.70のホストネームを取得、表示できています。

