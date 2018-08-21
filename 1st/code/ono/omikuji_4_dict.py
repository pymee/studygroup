#!/usr/bin/env python3
# coding: utf-8

import random

omikuji = {'大吉': 'すべてよし',
           '中吉': 'まあまあよし',
           '吉': 'よし',
           '凶': 'わるし'}
           
# 型の表示
print(type(omikuji))

# 項目の追加
omikuji['大凶'] = 'すべてわるし'

# 項目の変更
omikuji['中吉'] = 'まぁまぁよし'

# 項目の削除
del omikuji['凶']

# omikujiの項目を表示
print(omikuji)

# 辞書のアイテムをリストに変換
output_omikuji = list(omikuji.items())

# output_omikujiを表示
print(random.choice(output_omikuji))

# 型の表示
print(type(output_omikuji))