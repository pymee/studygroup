from email.message import EmailMessage
from email.generator import Generator

# 変数の設定
# 送信元、宛先、CCのメールアドレスを変数で定義してメールを作成してみよう！
subject = 'サービスメンテナンスのご連絡'
company = '株式会社A'
name = '佐藤'

# <会社名>と<宛名>の部分を関数で書き換えてみよう
message = """<会社名>　<宛名>様

お世話になっております。pymeeです。

いつも【サービスA】をご利用いただきありがとうございます。
以下日程にてサービスメンテナンスを実施いたします。

2020年12月30日 23:00 〜 12月31日 6:00

ご迷惑をおかけしますが、
メンテナンス時間は弊社サービスをご利用いただけませんので、
ご了承くださいませ。

以上です。よろしくお願いいたします。
"""

# メールを作成する
mail_data = EmailMessage()

# 送信元アドレスを設定する
mail_data['From'] = '送信元メールアドレス'

# 宛先アドレスを設定する
mail_data['To'] = '宛先メールアドレス'

# CCアドレスを設定する
mail_data['CC'] = 'CCのメールアドレス'

# 件名を設定する
mail_data['subject'] = subject

# 本文を設定する
mail_data.set_content(message)

# mail_dataの中身をみてみる
print(mail_data)

# 設定した内容をファイルに書き込む
with open('result/サービスメンテナンスのご連絡_<会社名>_<宛名>.eml'.replace('<会社名>',company).replace('<宛名>',name), 'w') as eml:
    eml_file = Generator(eml)
    eml_file.flatten(mail_data)

