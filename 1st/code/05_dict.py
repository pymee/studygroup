#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

omikuji = {'daikichi': '大吉 すべてよし',
           'chukichi': '中吉 まあまあよし',
           'shokichi': '小吉 よし',
           'kichi': '吉 少しよし',
           'kyo': '凶 わるし'
}

#辞書(omikuji)のkeyをランダム取得し、unsei_keyに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei_key = random.choice(list(omikuji.keys()))

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + omikuji[unsei_key] +'です!')
