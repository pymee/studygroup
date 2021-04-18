import csv
import os
import sys
from email.message import EmailMessage
from email.generator import Generator

#添付ファイルの有無を確認。該当範囲以外の数字もしくは数字以外が入ったらエラーで終了させる
try:
    mail_attach = input("添付ファイルを入れる場合は、「1」を不要の場合は「2」を入れてください。")
    mail_attach_int = int(mail_attach)
except ValueError:
    print("【エラー】数字の「1」もしくは「2」を入れてください。")
    sys.exit()

if mail_attach_int <= 0 or mail_attach_int >= 3 :
    print("【エラー】数字の「1」もしくは「2」を入れてください。")
    sys.exit()

# CSVファイルを読み込む
with open('address2.csv', 'r', encoding='shift_jis') as f:
    # 以下のフォーマットで値をコマンドプロンプトに表示させてみよう
    # 会社名: <会社名>, 宛名: <宛名>
    # リストlist_dataに値を追加して最後にリストをコマンドプロンプトに表示させてみよう
    csv_data = csv.reader(f)

    list_data = []
    for line in csv_data:
        list_data.append(line)

        # 変数の設定
        # 送信元、宛先、CCのメールアドレスを変数で定義してメールを作成してみよう！
        company = line[2]
        name = line[3]
        from_mail = 'pymee-support@example.com'
        to_mail = line[0]
        cc_mail = line[1]
        service = line[4]

        # サービス毎にフォルダを作る
        mail_path = "サービス_" + service
        if not os.path.exists(mail_path):
            os.mkdir(mail_path)

        # テキストファイルから本文を読み込み、<会社名>と<宛名>の部分を関数で書き換えてみよう
        with open("mail_honbun.txt","r", encoding='UTF-8')as re:
            message = re.read().format(company, name, service)

        # メールを作成する
        mail_data = EmailMessage()

        # 送信元アドレスを設定する
        mail_data['From'] = from_mail

        # 宛先アドレスを設定する
        mail_data['To'] = to_mail

        # CCアドレスを設定する
        mail_data['CC'] = cc_mail

        # 件名を設定する
        mail_data['subject'] = "サービスメンテナンスのご連絡{}".format(company)

        # 本文を設定する
        mail_data.set_content(message)

        # 設定した内容をファイルに書き込む
        with open(os.path.join(mail_path,'サービスメンテナンスのご連絡_{}_{}.eml'.format(company, name)), 'w') as eml:
            eml_file = Generator(eml)
            eml_file.flatten(mail_data)

#添付ファイル有だった場合はメールを作成する
        if mail_attach_int == 1:

            # テキストファイルから本文を読み込み、<会社名>と<宛名>の部分を関数で書き換えてみよう
            with open("mail_attach.txt", "r", encoding="utf-8")as re_a:
                att_message = re_a.read().format(company, name, service)

            # メールを作成する
            mail_data = EmailMessage()

            # 送信元アドレスを設定する
            mail_data['From'] = from_mail

            # 宛先アドレスを設定する
            mail_data['To'] = to_mail

            # CCアドレスを設定する
            mail_data['CC'] = cc_mail

            # 件名を設定する
            mail_data['subject'] = "【PW】サービスメンテナンスのご連絡{}".format(company)

            # 本文を設定する
            mail_data.set_content(att_message)

            with open(os.path.join(mail_path, '【PW】サービスメンテナンスのご連絡_{}_{}.eml'.format(company, name)), 'w') as eml:
                eml_file = Generator(eml)
                eml_file.flatten(mail_data)

#添付ファイルなしだった場合はそのまま終了する

print("メールの作成が完了しました。")
