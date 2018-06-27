#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 少しよし'
omikuji_4 = '吉 よし'
omikuji_5 = '凶 わるし'

# random.randintは()の中の数字からランダムで数字を選択してくれます
# 選択した数字をnumに代入
num = random.randrange(0,5)

# numに格納された数字によって出力される文字列を変更
if num == 0:
	unsei = omikuji_1
elif num == 1:
	unsei = omikuji_2
elif num == 2:
	unsei = omikuji_3
elif num == 3:
	unsei = omikuji_4
elif num == 4:
	unsei = omikuji_5	
else:
	unsei = ""
     
print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')