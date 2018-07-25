# モジュールをインポート
import random

# 辞書が内包されたリストを作成
omikuji = [{'all':'大吉! すべてよし。 ','work':'仕事運:プロジェクトは大成功！'},
		{'all':'中吉! まぁまぁよし。 ','work':'仕事運:定時で帰れます！'},
		{'all':'小吉! よし。 ','work':'仕事運:ミスなく過ごせます！'},
		{'all':'吉! 少しよし。 ','work':'仕事運:思ったよりも上手くいくかも'},
		{'all':'凶! わるし。 ','work':'仕事運:些細なミスが命取りに！'}]

# omikuji内の辞書からランダムで取得
unsei = random.choice(omikuji)

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei['all']+ '\n' + unsei['work'])
