# coding:utf-8
'''
作成日：2018/06/12
作成者：池田 虎太郎

【詳細】
乱数使用プログラム+入力プログラム
'''

#現在時刻を取得する為の準備
import datetime

#変数にそれぞれ「大吉」「中吉」「小吉」の文字列を格納
daikiti = "大吉"
tyukiti = "中吉"
syokiti = "小吉"

#現在時刻を取得し、3で割った余りをrandom変数へ格納
now = datetime.datetime.now() # => datetime.datetime(2017, 7, 1, 23, 15, 34, 309309)
random = now.microsecond % 3

#randomに格納された結果によって出力される文字列を変更
if random == 0:
    output = daikiti
elif random == 1:
    output = tyukiti
elif random == 2:
    output = syokiti
else:
    output = ""

#入力を促す文字列の準備
info = "名前を入力して下さい。"
#文字列の出力
print (info);

#文字列の入力
#入力された文字列をname変数へ格納
name = input()
#平文＋入力された文字列(name)＋乱数で決定した文字列(output)を結合して出力する。
print ("今日の"  + name + "さんの運勢は"  + output + "です。");