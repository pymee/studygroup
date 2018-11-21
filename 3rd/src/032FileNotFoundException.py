#! python3

#エラーが発生した際に別処理へ遷移させたい箇所をtry～exceptで囲む。
try:

#例文として存在しないファイルを指定
    output = open("exception.txt", "r",encoding="utf-8")

    for o in output:
        print (o);
        output.close()

#ファイルが見つからない時は以下のコードが実行される。
except FileNotFoundError:
    print("ファイル読み込みエラー！")
#その他のエラー発生時は以下のコードが実行される。
except:
    print("エラー！")
