#ランダムで値を取り出す為の準備
import random

#変数numの最初の数字を定義
num = 0

#while文で条件、および処理を定義「4じゃない間は変数numで0-9の乱数を表示する」
while num != 4:
    num = random.randint(0,9)
    print(num)