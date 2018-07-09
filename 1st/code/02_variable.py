#!/usr/bin/env python3
# coding: utf-8

# 変数に値(運勢)を代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_５ = '凶 わるし'

# unseiにdaikichiを代入
unsei = daikichi

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
