#!/usr/bin/python3.6
import sys
import random
import os
from datetime import datetime

#引数にファイルが一つ指定されていることをチェック
if len(sys.argv) != 2:
    sys.stderr.write('エラー:引数にファイルを一つ指定してください。\n')
    sys.exit(1)

#引数に読み込むファイルを指定してオープン
try:
    with open(sys.argv[1], "r",encoding="utf-8") as f:

#while実行前に定義、この時点でファイルの1行目を読み込み
        line = f.readline()

#whileで読み込んだ行を格納する空のリストを準備
        lines=[]

#引数ファイルを１行ずつ読み込んでリストに格納
        while line:
            lines.append(line)
            line = f.readline()
            if line == "":
                break

#例外をキャッチした場合の処理内容
except FileNotFoundError:
        sys.stderr.write("エラー:指定されたファイルが見つかりません。\n")
        sys.exit(1)
except PermissionError:
        sys.stderr.write("エラー:指定されたファイルに読み取り権限がありません。\n")
        sys.exit(1)

#おみくじの結果を格納したリストからランダムで１行をチョイス
kekka = random.choice(lines)

#ランダムでチョイスした１行（文字列）をカンマ区切りでリストに変換
kekkaList = kekka.split(',')

#出力するファイル名に付与する日付を取得
hizuke = datetime.now().strftime("%Y-%m-%d")

#出力ファイル名を指定
kekka_filename = r"./results/kekka_{0}.txt".format(hizuke)

#出力ファイル名でファイルオープンし結果を書き込み
try:
    f = open(kekka_filename,'x')
except FileExistsError:
        sys.stderr.write("エラー:同じ名前のファイルが既に存在しています。\n")
        sys.exit(1)
except FileNotFoundError:
        sys.stderr.write("エラー:ディレクトリが見つかりません。\n")
        sys.exit(1)
except PermissionError:
        sys.stderr.write("エラー:指定されたファイルに書き込み権限がありません。\n")

#出力ファイル名でファイルオープンし結果を書き込み
f = open(kekka_filename,'w')
f.write("===============================\n")
for i in kekkaList:
    f.write(i)
    f.write("\n")
f.write(hizuke)
f.write("\n")
f.write("===============================\n")
f.close()

print("おみくじの結果を{0}に書込みました！".format(kekka_filename))
