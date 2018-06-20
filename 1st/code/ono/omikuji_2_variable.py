# coding: utf-8

import random

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 少しよし'
omikuji_4 = '吉 よし'
omikuji_5 = '凶 わるし'

# 変数をランダムで1つ表示させる
fortune = random.choice([omikuji_1,omikuji_2,omikuji_3,omikuji_4,omikuji_5])

# 結果を出力
print(fortune)