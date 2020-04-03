#!/usr/bin/python3
# coding:utf-8

import sys

# ˆø”‚©‚ç”š‚ğæ“¾
num1 = sys.argv[1]
num2 = sys.argv[2]

# ‘«‚µZ
wa = int(num1) + int(num2)
print(str(num1) + " { " + str(num2) + " = " + str(wa))

# ˆø‚«Z
if int(num1) >= int(num2) :
    sa = int(num1) - int(num2)
    print(str(num1) + " | " + str(num2) + " = " + str(sa))
else :
    sa = int(num2) - int(num1)
    print(str(num2) + " | " + str(num1) + " = " + str(sa))

# Š|‚¯Z
seki = int(num1) * int(num2)
print(str(num1) + " ~ " + str(num2) + " = " + str(seki))

# Š„‚èZ
if int(num1) >= int(num2) :
    try :
        sho = int(num1) // int(num2)
        rem = int(num1) % int(num2)
        print(str(num1) + " € " + str(num2) + " = " + str(sho) + " ‚ ‚Ü‚è " + str(rem))
    except ZeroDivisionError :
        print(str(num1) + " € " + str(num2) + " = " + "yƒGƒ‰[z0‚ÅœZ‚µ‚Ä‚¢‚Ü‚·")
else :
    try :
        sho = int(num2) // int(num1)
        rem = int(num2) % int(num1)
        print(str(num2) + " € " + str(num1) + " = " + str(sho) + " ‚ ‚Ü‚è " + str(rem))
    except ZeroDivisionError :
        print(str(num2) + " € " + str(num1) + " = " + "yƒGƒ‰[z0‚ÅœZ‚µ‚Ä‚¢‚Ü‚·")