#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
		   '中吉 まあまあよし',
		   '小吉 すこしよし', 
		   '吉 よし',
		   '凶 わるし',
		   ]

#ランダムでおみくじを表示
unsei = random.choice(omikuji)

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
