#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 代入
daikichi = '大吉 すべてよし'
chukichi = '中吉 まあまあよし'
shokichi = '小吉 よし'
kichi = '吉 すこしよし'
kyo = '凶 わるし'

# random.randrangeは()にしていた範囲からランダムに要素を返します
# 選択した数字をnumに代入
num = random.randrange(0,6)

# numに格納された数字によって出力される文字列を変更
if num == 0:
	unsei = daikichi
elif num == 1:
	unsei = chukichi
elif num == 2:
	unsei = shokichi
elif num == 3:
	unsei = kichi
elif num == 4:
	unsei = kyo
else:
	unsei = ""

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
