#!/usr/bin/env python3
# coding: utf-8

# 変数に値(運勢)を代入
daikichi = '大吉 すべてよし'
chukichi = '中吉 まあまあよし'
shokichi = '小吉 よし'
kichi = '吉 すこしよし'
kyo = '凶 わるし'

# unseiにdaikichiを代入
unsei = daikichi

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
