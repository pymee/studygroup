import sys
#ランダムで値を取り出す為の準備
import random

#エラーが発生した際に別処理へ遷移させたい箇所をtry～exceptで囲む。
try:

#おみくじ用ファイルを読み込む
    daikiti = open("daikiti.txt", "r",encoding="utf-8")
    kiti    = open("kiti.txt", "r",encoding="utf-8")
    kyo     = open("kyo.txt", "r",encoding="utf-8")

#読み込んだおみくじ用ファイルを辞書型でまとめる
    inputOmikuji = {"大吉":daikiti,
                    "吉":kiti,
                    "凶":kyo}

#ランダムで選択する為のキーとなる単語をリストで用意
    omikujiList = inputOmikuji.keys()

#omikujiListの中からランダムで一つ選ぶ
    randomOmikuji = random.choice(list(omikujiList))

#omikujiListからランダムに選んだ運勢(文字列)をキーにしてinputOmikujiにセットしたテキストファイルの中身から選んだ文字列に対応するファイルの中身を読み込む。
    selectOmikuji = inputOmikuji[randomOmikuji]

#読み込んだファイルの中身を1行ずつ取り出す。
    for selectLine in selectOmikuji:
        print (selectLine, end='');

    print('\n')

#ファイルが見つからない時は以下のコードが実行される。
except FileNotFoundError:
    print("ファイル読み込みエラー！")
    print(sys.exc_info())
#その他のエラー発生時は以下のコードが実行される。
except:
    print("その他のエラー！")
    print(sys.exc_info())
else:
    print('\nおみくじの結果はどうでしたか？')
#以下のコードはどんな場合でも実行される。
finally:
    if 'daikiti' in locals():
        daikiti.close()
    if 'kiti' in locals():
        kiti.close()
    if 'kyo' in locals():
        kyo.close()