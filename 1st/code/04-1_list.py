#!/usr/bin/env python3
# coding: utf-8

# typeや追加、削除、特定の要素の確認については、インタプリタで確認

# モジュールをインポート
import random  

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
           '中吉 まあまあよし',
           '小吉 すこしよし',
           '吉 よし',
           '凶 わるし',
           '大凶 すべてわるし'
           ]

#乱数を生成
num = random.randrange(0,6)

# omikuji[num]をunseiに代入
unsei = omikuji[num]

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')