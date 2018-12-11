#読み込むファイルを指定。
#この書式で記載すると以下の通りに値が格納される。
#　・ファイル読み込み元：inputSample.txt
#　・ファイルから読み込んだ中身の格納先：inputAll(一行ずつリスト形式で格納される)
inputAll = open("inputSample.txt", "r",encoding="utf-8")

#ファイルから読み込んだ中身を一行ずつfor文で出力する。
for inputLine in inputAll:
    print (inputLine, end='');

#見やすいように最後に改行を入れる
print('\n')

#ファイルを読み込んだ後はクローズ処理を記載する。
#これを書かないとメモリにゴミが残る。(動作が重くなっていく)
inputAll.close()