from email.message import EmailMessage
from email.generator import Generator

import csv

# CSVファイルを読み込み
with open('data/address2.csv', 'r') as f:
    # 以下のフォーマットで値をコマンドプロンプトに表示させてみよう
    # 会社名: <会社名>, 宛名: <宛名>
    # リストlist_dataに値を追加して最後にリストをコマンドプロンプトに表示させてみよう
    csv_data = csv.reader(f)

    csv_list = []
    for line in csv_data:
        csv_list.append(line)


# メールで使用する共通部分のデータを変数に格納
subject = 'サービスメンテナンスのご連絡'
from_mail = 'pymee-support@example.com'

# csv_listから1行づつデータを取り出し、メールデータを作成する
for line in csv_list:
    # csv_listからのデータを変数に格納する
    company = line[2]   # 会社名
    name = line[3]      # 宛名
    to_mail = line[0]   # 宛先メールアドレス
    cc_mail = line[1]   # CCのメールアドレス

    # 本文の<会社名>と<宛名>部分を置換する
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


    # 設定した内容をファイルに書き込む
    with open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',company).replace('<宛名>',name), 'w') as eml:
        eml_file = Generator(eml)
        eml_file.flatten(mail_data)
