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
    print(str(num1) + " ＋ " + str(num2) + " = " + str(wa))

    # 引き算
    if num1 >= num2 :
        sa = int(num1) - int(num2)
        print(str(num1) + " － " + str(num2) + " = " + str(sa))
    else :
        sa = int(num2) - int(num1)
        print(str(num2) + " － " + str(num1) + " = " + str(sa))

    # 掛け算
    seki = int(num1) * int(num2)
    print(str(num1) + " × " + str(num2) + " = " + str(seki))

    # 割り算
    if num1 >= num2 :
        sho = int(num1) // int(num2)
        rem = int(num1) % int(num2)
        print(str(num1) + " ÷ " + str(num2) + " = " + str(sho) + " あまり " + str(rem))
    else :
        sho = int(num2) / int(num1)
        rem = int(num2) % int(num1)
        print(str(num2) + " ÷ " + str(num1) + " = " + str(sho) + " あまり " + str(rem))

except ValueError :
    print("数字がふたつ入力されなかったので、何もせずにプログラムを終了します。")