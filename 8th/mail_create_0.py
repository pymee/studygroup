import csv
from email.message import EmailMessage
from email.generator import Generator

# CSVファイルを読み込む
with open('data/address0.csv', 'r') as f:
    csv_data = csv.reader(f)

    data = []
    for line in csv_data:
        data.append(line)


for line in data:
    # メールを作成する
    mail_data = EmailMessage()

    # 送信元アドレスを設定する
    from_add = 'yui.sano@example.com'
    mail_data['From'] = from_add

    # 宛先アドレスを設定する
    mail_data['To'] = line[0]

    # CCアドレスを設定する
    mail_data['CC'] = line[1]

    # 件名を設定する
    subject = 'サービスメンテナンスのご連絡'
    mail_data['subject'] = subject

    # 本文を読み込む
    with open('data/message.txt', 'r') as f :
        message = f.read()

    # 本文の中身を書き換える
    change_message = message.replace('<会社名>', line[2]).replace('<宛名>', line[3])

    # 本文を設定する
    mail_data.set_content(change_message)

    # 設定した内容をファイルに書き込む
    with open(f'result/{subject}_{line[2]}_{line[3]}様.eml', "w") as eml:
        eml_file = Generator(eml)
        eml_file.flatten(mail_data)
