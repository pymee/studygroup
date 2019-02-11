import random

#ファイルを格納するためのリストを準備
WhileList = []

#読み込むファイルを指定してオープン
f = open("while.txt", "r",encoding="utf-8")

#readline()で1行ずつ読み込み
line = f.readline()

#while文で処理を定義「取り出した行が "EOF\n" 以外なら1行ずつWhileListに格納」
while line != "EOF\n":
	WhileList.append(line)
	line = f.readline()

#読み込んだファイルをクローズ
f.close

#ランダムでリストから結果を取り出し
kekka = random.choice(WhileList)

#結果を表示
print(kekka)