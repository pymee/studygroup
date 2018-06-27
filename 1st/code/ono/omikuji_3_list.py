#!/usr/bin/env python3
# coding: utf-8

import random  

omikuji = ['大吉 すべてよし', '中吉 まあまあよし', '吉 よし' , '凶 わるし'] 

# 後ろに追加
omikuji.append("大凶 すべてわるし")

# 任意の場所に追加
omikuji.insert(2, "小吉 すこしよし")

# 要素を一つ削除
omikuji.remove("凶 わるし")

#ランダムでおみくじを表示
print(random.choice(omikuji))
