# キーボードから数字を取得
num1 = input("ひとつめの数字を入力してください。")
num2 = input("ふたつめの数字を入力してください。")

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
        sho = int(num1) // int(num2)
        rem = int(num1) % int(num2)
        print('{} ÷ {} = {} あまり {}'.format(num1,num2,sho,rem))
    else :
        sho = int(num2) // int(num1)
        rem = int(num2) % int(num1)
        print('{} ÷ {} = {} あまり {}'.format(num2,num1,sho,rem))

except ValueError :
    print("数字がふたつ入力されなかったので、何もせずにプログラムを終了します。")