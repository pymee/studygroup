#!/usr/bin/env python3
# coding: utf-8

import random

fortune = [{'運勢':'運勢は大吉! すべてよし。仕事運は、全て上手くいく'},
		{'運勢':'運勢は中吉! まぁまぁよし。 仕事運は、努力すれば実る'},
		{'運勢':'運勢は吉! よし。 仕事運は、なかなか実らず'},
		{'運勢':'運勢は凶! わるし。 仕事運は、全てが上手くいかず'}]
		
# 運勢の中からランダムで選択
unsei = random.choice([x['運勢'] for x in fortune])

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print('{} さんの運勢は、'.format(name) + unsei + 'となります!')

# 運勢が吉以上かで判断
if '吉' in unsei:
	print('おめでとうございます。')
else:
	print('またお願いします。')