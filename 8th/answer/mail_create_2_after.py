import csv

# CSVファイルを読み込む
with open('data/address2.csv', 'r') as f:
    # 以下のフォーマットで値をコマンドプロンプトに表示させてみよう
    # 会社名: <会社名>, 宛名: <宛名>
    # リストlist_dataに値を追加して最後にリストをコマンドプロンプトに表示させてみよう
    csv_data = csv.reader(f)

    csv_list = []
    for line in csv_data:
        print('会社名: {}, 宛名: {}'.format(line[2], line[3]))
        csv_list.append(line)

print(csv_list)

