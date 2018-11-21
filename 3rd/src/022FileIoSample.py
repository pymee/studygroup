#! python3

#読み込むファイルを指定。
#ファイル読み込み元：outputSample.txt
output = open("outputSample.txt", "r",encoding="utf-8")

for o in output:
    print (o);

output.close()