#!/usr/bin/env python3
# coding: utf-8

import random

fortune = {'1':'運勢は大吉! すべてよし。仕事運は、全て上手くいく',
		   '2':'運勢は中吉! まぁまぁよし。 仕事運は、努力すれば実る',
		   '3':'運勢は吉! よし。 仕事運は、なかなか実らず',
		   '4':'運勢は凶! わるし。 仕事運は、全てが上手くいかず',
           }
           
#forでkeys,valuesを取得
for k,v in fortune.items():
	print(k,v)
	
# ネスト(入れ子)の辞書
fortune_2 = {'1'
              :{'zentai':'大吉! すべてよし','shigoto':'仕事運 全て上手くいく'},
	  	     '2'
	  	      :{'zentai':'中吉! まぁまぁよし','shigoto':'仕事運 努力すれば実る'},
        	 '3'
		      :{'zentai':'吉! よし','shigoto':'仕事運 なかなか実らず'},
	         '4'
		     :{'zentai':'凶! わるし','shigoto':'仕事運 全てが上手くいかず'}
            }

           
#forでkeys,valuesを取得
for k,v in fortune_2.items():
	unsei = v['zentai'],v['shigoto']
	print(unsei)