#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
           '中吉 まあまあよし',
           '小吉 よし',
           '吉 すこしよし',
           '凶 わるし',
           ]
# 乱数を生成
num = random.randrange(0,5)

# omikuji[num]をunseiに代入
unsei = omikuji[num]

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
