#!/usr/bin/env python3
# coding: utf-8

# typeや追加、削除、特定の要素の確認については、インタプリタで確認。

# モジュールをインポート
import random

omikuji = {'運勢1': '大吉 すべてよし',
           '運勢2': '中吉 まあまあよし',
           '運勢3': '小吉 よし',
           '運勢4': '吉 少しよし',
           '運勢5': '凶 わるし'
}

#辞書(omikuji)のkeyをランダム取得し、unsei_keyに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei_key = random.choice(list(omikuji.keys()))

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + omikuji[unsei_key] +'です!')
