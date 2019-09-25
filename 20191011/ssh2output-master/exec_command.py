import csv
import os
import sys

from libs import SSHConnector
from libs import OutPutTextCreator


def exec_command(args):
    # 出力用テキストを生成するためのクラスをインスタンス化
    optc = OutPutTextCreator.OutPutTextCreator()
    result_text = ""

    # コマンドライン引数で指定したファイルがなかったらここで終了させる
    if not os.path.exists(args.csv_file):
        print("コマンドライン引数で指定したCSVファイルがありません。", file=sys.stderr)
        sys.exit(1)

    # csvファイルを開いてIPアドレスとか取り出す
    with open(args.csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            command = row[3]
            if not row[0] == "":
                ipaddr = row[0]
                username = row[1]
                password = row[2]
                optc.set_remote_info(ipaddr, username, command)

            # paramikoでサーバへ接続してコマンドを実行後標準出力を取得
            prmk = SSHConnector.SSHConnector(hostname=ipaddr, username=username, password=password)
            sout = prmk.send_command(command)

            result_text += optc.replace_content(sout)

    return result_text
