#!/usr/bin/python3
# coding:utf-8

# ƒL[ƒ{[ƒh‚©‚ç”š‚ğæ“¾
num1 = input("‚Ğ‚Æ‚Â‚ß‚Ì”š‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢B")
num2 = input("‚Ó‚½‚Â‚ß‚Ì”š‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢B")

# ‘«‚µZ
wa = int(num1) + int(num2)
print(str(num1) + " { " + str(num2) + " = " + str(wa))

# ˆø‚«Z
if num1 >= num2 :
    sa = int(num1) - int(num2)
    print(str(num1) + " | " + str(num2) + " = " + str(sa))
else :
    sa = int(num2) - int(num1)
    print(str(num2) + " | " + str(num1) + " = " + str(sa))

# Š|‚¯Z
seki = int(num1) * int(num2)
print(str(num1) + " ~ " + str(num2) + " = " + str(seki))

# Š„‚èZ
if num1 >= num2 :
    sho = int(num1) // int(num2)
    rem = int(num1) % int(num2)
    print(str(num1) + " € " + str(num2) + " = " + str(sho) + " ‚ ‚Ü‚è " + str(rem))
else :
    sho = int(num2) / int(num1)
    rem = int(num2) % int(num1)
    print(str(num2) + " € " + str(num1) + " = " + str(sho) + " ‚ ‚Ü‚è " + str(rem))