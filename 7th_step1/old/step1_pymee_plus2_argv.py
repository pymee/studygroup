#!/usr/bin/python3
# coding:utf-8

import sys

# 引数から数字を取得
num1 = sys.argv[1]
num2 = sys.argv[2]

# 足し算
wa = int(num1) + int(num2)
print(str(num1) + " ＋ " + str(num2) + " = " + str(wa))

# 引き算
if int(num1) >= int(num2) :
    sa = int(num1) - int(num2)
    print(str(num1) + " − " + str(num2) + " = " + str(sa))
else :
    sa = int(num2) - int(num1)
    print(str(num2) + " − " + str(num1) + " = " + str(sa))

# 掛け算
seki = int(num1) * int(num2)
print(str(num1) + " × " + str(num2) + " = " + str(seki))

# 割り算
if int(num1) >= int(num2) :
    try :
        sho = int(num1) // int(num2)
        rem = int(num1) % int(num2)
        print(str(num1) + " ÷ " + str(num2) + " = " + str(sho) + " あまり " + str(rem))
    except ZeroDivisionError :
        print(str(num1) + " ÷ " + str(num2) + " = " + "【エラー】0で除算しています")
else :
    try :
        sho = int(num2) // int(num1)
        rem = int(num2) % int(num1)
        print(str(num2) + " ÷ " + str(num1) + " = " + str(sho) + " あまり " + str(rem))
    except ZeroDivisionError :
        print(str(num2) + " ÷ " + str(num1) + " = " + "【エラー】0で除算しています")