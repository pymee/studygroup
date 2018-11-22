#! python3

#ランダムで値を取り出す為の準備
import random #

#エラーが発生した際に別処理へ遷移させたい箇所をtry～exceptで囲む。
try:

#おみくじ用ファイルを読み込む
    daikiti = open("daikiti.txt", "r",encoding="utf-8")
    kiti    = open("kiti.txt", "r",encoding="utf-8")
    kyo     = open("kyo.txt", "r",encoding="utf-8")

#読み込んだおみくじ用ファイルを辞書型でまとめる
    input = {"大吉":daikiti,
              "吉":kiti,
              "凶":kyo}

#ランダムで選択する為のキーとなる単語をリストで用意
    omikujiList = ["大吉","吉","凶"]

#omikujiListの中からランダムで一つ選ぶ
    selectOmikuji = random.choice(omikujiList)

#omikujiListからランダムに選んだ運勢(文字列)をキーにしてinputにセットしたテキストファイルの中身から選んだ文字列に対応するファイルの中身を読み込む。
    output = input[selectOmikuji]

#読み込んだファイルの中身を1行ずつ取り出す。
    for o in output:
        print (o);

#クローズ処理
    output.close()

#ファイルが見つからない時は以下のコードが実行される。
except FileNotFoundError:
    print("ファイル読み込みエラー！")
#その他のエラー発生時は以下のコードが実行される。
except:
    print("エラー！")
