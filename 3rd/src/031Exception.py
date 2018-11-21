#! python3

#エラーが発生した際に別処理へ遷移させたい箇所をtry～exceptで囲む。
#基本的に全部でいい。
try:

#例文として存在しないファイルを指定
    output = open("exception.txt", "r",encoding="utf-8")

    for o in output:
        print (o);
        output.close()

#上記のexception.txtが存在しない為、エラーが発生して以下のexceptと記載された箇所の処理が実行される。
#エラーが発生しなかった場合はexcept句に記載されたコードは実行されない。
except:
    print("エラー！")