import sys

#引数に読み込むファイルを指定してオープン
omikuji = open(sys.argv[1], "r",encoding="utf-8")

#書き込み先のファイルを新規作成してオープン
f = open('write_kekka.txt','x')

#上部飾りを挿入
f.write("===============================\n")

#ファイルから読み込んだリストを一行ずつ最終行までfor文で書き込み
for i in omikuji:
    f.write(i)

#改行して下部飾りを挿入
f.write("\n")
f.write("===============================\n")

#ファイルクローズ
f.close()