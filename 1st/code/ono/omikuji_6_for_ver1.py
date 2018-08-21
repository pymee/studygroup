#!/usr/bin/env python3
# coding: utf-8

import random

fortune = {'1'
              :{'zentai':'大吉! すべてよし','shigoto':'仕事運 全て上手くいく'},
	  	   '2'
	  	      :{'zentai':'中吉! まぁまぁよし','shigoto':'仕事運 努力すれば実る'},
		   '3'
		      :{'zentai':'吉! よし','shigoto':'仕事運 なかなか実らず'},
	       '4'
		     :{'zentai':'凶! わるし','shigoto':'仕事運 全てが上手くいかず'}
            }

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')
print('{} さんの運勢は、'.format(name))

# 運勢をランダムで取得
num = list(fortune)
for k,v in (fortune[random.choice(num)].items()):
	unsei = v
	# 結果を出力
	print(unsei + 'となります!')