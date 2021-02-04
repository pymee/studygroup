import csv
import os
import sys
from email.message import EmailMessage
from email.generator import Generator
from data import read_txt
from data import create_mail

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

with open('address2.csv', 'r', encoding="shift-jis") as f:
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
        honbun = read_txt("mail_honbun.txt")
        service = line[4]
        subject = "サービスメンテナンスのご連絡{}".format(company)

        # サービス毎にフォルダを作る
        mail_path = "サービス_" + service
        if not os.path.exists(mail_path):
            os.mkdir(mail_path)

        mail_data = create_mail(subject,to_mail,cc_mail,from_mail,honbun.format(company,name,service))

        # 設定した内容をファイルに書き込む
        with open(os.path.join(mail_path,'サービスメンテナンスのご連絡_{}_{}.eml'.format(company, name)), 'w') as eml:
            eml_file = Generator(eml)
            eml_file.flatten(mail_data)

#添付ファイル有だった場合はメールを作成する
        if mail_attach_int == 1:
            honbun = read_txt("mail_attach.txt")
            subject = "【PW】サービスメンテナンスのご連絡{}".format(company)

            mail_data = create_mail(subject, to_mail, cc_mail, from_mail, honbun.format(company, name, service))

            with open(os.path.join(mail_path, '【PW】サービスメンテナンスのご連絡_{}_{}.eml'.format(company, name)), 'w') as eml:
                eml_file = Generator(eml)
                eml_file.flatten(mail_data)

#添付ファイルなしだった場合はそのまま終了する

print("メールの作成が完了しました。")