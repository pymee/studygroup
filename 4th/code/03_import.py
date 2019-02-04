import sys

#datetimeモジュールからdatetimeクラスをimport
from datetime import datetime

#引数に読み込むファイルを指定してオープン
omikuji = open(sys.argv[1], "r",encoding="utf-8")

#現在時刻を年-月-日として文字列に変換する
hizuke = datetime.now().strftime("%Y-%m-%d")

#書き込み先のファイルを新規作成してオープン
f = open('import_kekka.txt','x')

#上部飾りを挿入
f.write("===============================\n")

#ファイルから読み込んだリストを一行ずつ最終行までfor文で書き込み
for i in omikuji:
    f.write(i)

#改行を挿入    
f.write("\n")

#日付を挿入
f.write(hizuke)

#改行して下部飾りを挿入
f.write("\n")
f.write("===============================\n")

#ファイルクローズ
f.close()

