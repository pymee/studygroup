#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 辞書が内包されたリストを作成
fortune = [{'all':'大吉! すべてよし。 ','work':'仕事運:プロジェクトは大成功！'},
		{'all':'中吉! まぁまぁよし。 ','work':'仕事運:定時で帰れます！'},
		{'all':'吉! よし。 ','work':'仕事運:ミスなく過ごせます！'},
		{'all':'小吉! 少しよし。 ','work':'仕事運:思ったよりも上手くいくかも'},
		{'all':'凶! わるし。 ','work':'仕事運:些細なミスが命取りに！'}]
		
# fortune内の辞書からランダムで取得
luck = random.choice(fortune)

# 辞書内のvalue(値)をunseiに代入　\nは改行コード
unsei = luck['all']+ '\n' + luck['work'] #辞書名[key]でvalueの表示

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei )