#読み込むファイルを指定。
#ファイル読み込み元：inputSample.txt
inputAll = open("inputSample.txt", "r",encoding="utf-8")

for inputLine in inputAll:
    print (inputLine, end='');

inputAll.close()