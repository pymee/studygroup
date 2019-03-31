import sys
import random
import os
from datetime import datetime

#引数にファイルが一つ指定されていることをチェック
if len(sys.argv) != 2:
    sys.stderr.write('エラー:引数にファイルを一つ指定してください。\n')
    sys.exit(1)

#ファイルを格納するためのリストを準備
KekkaList = []

#引数に読み込むファイルを指定してオープン1行ずつリストに格納
try:
    f = open(sys.argv[1], "r",encoding="utf-8")
    line = f.readline()
    while line != "EOF\n":
        KekkaList.append(line)
        line = f.readline()
    f.close

#例外をキャッチした場合の処理内容
except FileNotFoundError:
    sys.stderr.write("エラー:指定されたファイルが見つかりません。\n")
    sys.exit(1)
except:
    sys.stderr.write("エラー:その他のエラー。\n")
    sys.exit(1)

#ランダムでリストから結果を取り出し
kekka = random.choice(KekkaList)

#取り出した結果をカンマ区切りでリスト化
unsei = kekka.split(",")

#出力するファイル名に付与する日付を取得
hizuke = datetime.now().strftime("%Y-%m-%d")

#出力ファイル名を指定
unsei_filename = r"./results/unsei_{0}.txt".format(hizuke)

#出力ファイル名でファイルオープンし結果を書き込み
try:
    f = open(unsei_filename,'x')

#例外をキャッチした場合の処理内容
except FileExistsError:
        sys.stderr.write("エラー:同じ名前のファイルが既に存在しています。\n")
        sys.exit(1)
except FileNotFoundError:
        sys.stderr.write("エラー:ディレクトリが見つかりません。\n")
        sys.exit(1)

#おみくじの結果を書き込み
f.write("===============================\n")
for i in unsei:
    f.write(i)
    f.write("\n")
f.write(hizuke)
f.write("\n")
f.write("===============================\n")
f.close()

print("おみくじの結果を{0}に書込みました！".format(unsei_filename))
