#! python3

#読み込むファイルを指定。
#この書式で記載すると以下の通りに値が格納される。
#ファイル読み込み元：outputSample.txt
#読み込んだ値の格納先：output(リスト形式の変数)
output = open("outputSample.txt", "r",encoding="utf-8")

#ファイルから読み込んだ情報を一行ずつfor文で出力する。
for o in output:
    print (o);

#ファイルを読み込んだ後はクローズ処理を記載する。
#これを書かないとメモリにゴミが残る。(動作が重くなっていく)
output.close()