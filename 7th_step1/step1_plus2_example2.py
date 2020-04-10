import sys

# 引数の数チェック
if len(sys.argv) != 3 :
    print("計算用の引数が2つ指定されていないため、何もせずにプログラムを終了します。")
    exit()

# 引数から数字を取得
num1 = sys.argv[1]
num2 = sys.argv[2]

try :
    # 足し算
    wa = int(num1) + int(num2)
    print('{} ＋ {} = {}'.format(num1,num2,wa))

    # 引き算
    if int(num1) >= int(num2) :
        sa = int(num1) - int(num2)
        print('{} － {} = {}'.format(num1,num2,sa))
    else :
        sa = int(num2) - int(num1)
        print('{} － {} = {}'.format(num2,num1,sa))

    # 掛け算
    seki = int(num1) * int(num2)
    print('{} × {} = {}'.format(num1,num2,seki))

    # 割り算
    if int(num1) >= int(num2) :
        try :
            sho = int(num1) // int(num2)
            rem = int(num1) % int(num2)
            print('{} ÷ {} = {} あまり {}'.format(num1,num2,sho,rem))
        except ZeroDivisionError :
            print('{} ÷ {} = 【エラー】0で除算しています'.format(num1,num2))
    else :
        try :
            sho = int(num2) // int(num1)
            rem = int(num2) % int(num1)
            print('{} ÷ {} = {} あまり {}'.format(num2,num1,sho,rem))
        except ZeroDivisionError :
            print('{} ÷ {} = 【エラー】0で除算しています'.format(num2,num1))

except ValueError :
    print("数字がふたつ入力されなかったので、何もせずにプログラムを終了します。")