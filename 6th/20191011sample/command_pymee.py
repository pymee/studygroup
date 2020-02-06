import csv
import os
import socket
import string
import sys
from datetime import datetime

import paramiko

# コマンドライン引数の数のチェック
if len(sys.argv) <= 1:
    print("Usage: {} <csvfile>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

# csvファイルのパスを変数に格納
csv_file_path = sys.argv[1]

# コマンドライン引数で指定したcsvファイルがなければ終了させる
if not os.path.exists(csv_file_path):
    print("ERROR: CSVファイルが見つかりません", file=sys.stderr)
    sys.exit(1)

# CSVファイルが空だったら終了させる
if os.path.getsize(csv_file_path) == 0:
    print("ERROR: ファイルが空の可能性があります。", file=sys.stderr)
    sys.exit(1)

# Paramikoをインスタンス化して初期設定とか済ませておく
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 出力用のテンプレートを生成
templates_text = string.Template("""\
==============================
IPアドレス: $ipaddr
ログインユーザ: $username
実行時刻: $nowtime
==============================
$command
$command_result

""")

# 出力用の変数を定義
contents = ""

# CSVファイルを開いてIPアドレス、ユーザ名、パスワード、コマンドを取り出したあとにコマンドを実行して出力テキストを生成
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

		# CSVファイルの行数分繰り返す
		# SSHに必要な情報を取得し、変数に代入
    for row in csv_reader:
        if not (row[0] == "" and row[1] == "" or row[0] == "" and row[1] == "" and row[2] == ""):
            hostname = row[0]
            username = row[1]
            password = row[2]
        command = row[3]

        # サーバに接続
        try:
            ssh.connect(hostname=hostname, username=username, password=password,
                        port=22, timeout=10.0, look_for_keys=False)
        except paramiko.ssh_exception.AuthenticationException as e:
            print("ERROR: SSH認証に失敗しました。", file=sys.stderr)
            sys.exit(1)
        except paramiko.ssh_exception.NoValidConnectionsError:
            print("ERROR: 接続エラー。", file=sys.stderr)
            sys.exit(1)
        except socket.timeout:
            print("ERROR: タイムアウトしました。", file=sys.stderr)
            sys.exit(1)

        # ホスト名を取得 Linuxの $HOSTNAME 環境変数でホスト名を取得
        stdin, stdout, stderr = ssh.exec_command("echo $HOSTNAME")
        server_hostname = stdout.readline().strip("\n")

        # プロンプトの構築
        prompt = "[{user}@{hostname}]".format(user=username, hostname=server_hostname) 
        
        # 三項演算子を使用して一行でif-elseを書く
        prompt += "# " if username == "root" else "$ "

        # コマンド発行
        stdin, stdout, stderr = ssh.exec_command(command)

        command_result = ""

				# stdoutからコマンド実行結果を取り出し、出力ファイル用に整形
        for i in stdout:
            command_result += i.strip('\n') + '\n'

        contents += templates_text.substitute(ipaddr=hostname, username=username,
                                              nowtime=datetime.now().strftime("%H:%M"),
                                              command=prompt+command, command_result=command_result)

        # 念の為コネクションをクローズしておく
        ssh.close()

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
