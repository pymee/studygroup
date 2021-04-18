import csv

# CSVファイルを開く
with open('data/address2.csv', 'r') as f:
    # csvファイルのデータを読み込む
    csv_data = csv.reader(f)

    # csv_dataの１行分のデータをlineに格納する
    for line in csv_data:
        # lineを表示させる
        print('lineの中身：{}'.format(line))
#        print('宛先メールアドレス：{}'.format(line[0]))
#        print('CCメールアドレス：{}'.format(line[1]))
        print('------')

# ここでcsv_dataを読み込みができない
#for line in csv_data:
#    print('lineの中身：{}'.format(line))
#    print('------')
