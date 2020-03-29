# モジュールをインポート
import sys
import csv
import os

# コマンド引数の個数を代入
num_csv_file = len(sys.argv)

# コマンド引数が指定されてない場合は処理終了
if num_csv_file == 1:
    print('実行時にcsvファイルを指定して下さい。', file=sys.stderr)
    sys.exit(1)
elif num_csv_file >= 3:
    print('指定可能なcsvファイルは1つだけです。', file=sys.stderr)
    sys.exit(1)

# 入力ファイルを引数に代入
csv_file = sys.argv[1]

# 指定したcsvファイルが存在しない場合は処理終了
if not os.path.exists(csv_file):
    print('指定されたcsvファイルは存在しません。', file=sys.stderr)
    sys.exit(1)

# 指定したcsvファイルが空の場合は処理終了
if os.path.getsize(csv_file) == 0 :
    print('指定されたcsvファイルは空です。', file=sys.stderr)
    sys.exit(1)

# csvファイルを開きリストに変換する
tmp_csv_file =  open(csv_file, 'r')
input_data = csv.reader(tmp_csv_file)

# csvをもとに以下のデータを作成する
# output_data = [
#   (ip1, user1) : {'ip' : ip1, 'user' : user1, 'command' : [command1, command2] },
#   (ip2, user2) : {'ip' : ip2, 'user' : user2, 'command' : [command1, command2] },
#   ]
old_ip = ''
old_user = ''
output_data = {}
for line in input_data:
    ip, user, command = line[0], line[1], line[3]
    # (ip, user)のタプルを作成する、データが空の場合は前回のものを使用
    if ip == '':
        tmp_key = (old_ip, old_user)
    else:
        tmp_key = (ip, user)
    # (ip, user)が存在する場合はコマンドを追加、ない場合は新しくデータを作成
    if tmp_key in output_data:
        output_data[tmp_key]["command"].append(command)
    else:
        output_data[tmp_key] = {'ip': ip, 'user': user, 'command':[command]}
    # 以前のデータを更新する
    old_ip, old_user = ip, user

tmp_csv_file.close()

# output_dataをファイルに書き込む
for data in output_data.values():
    # データを変数に格納する
    ip = data['ip']
    user = data['user']
    command_list = data['command']

    # 同名の出力ファイルが存在しているか確認する
    output_file_name = f'command_{ip}.txt'
    if os.path.exists(output_file_name):
        print(f'同名の出力ファイル({output_file_name})が存在しています。', file = sys.stderr)
        sys.exit(1)

    # output_dataをファイルに書き込む
    with open( output_file_name, 'a') as output_file:
        output_file.write(f'ssh {ip}@{user}\n')

        for command in command_list:
            output_data.write(command + '\n')

        output_data.write('\n')

print('処理が正常に完了しました。')
