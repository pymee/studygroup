import unittest
import sys
import os
import subprocess
import filecmp


# 入力ファイルのテスト項目
class TestInputFile(unittest.TestCase):
    # csvファイルが指定されていない場合
    def test_not_specified(self):
        command = ['python3','step2_pymee.py']
        output = subprocess.run(command,
                                capture_output = True,
                                encoding='utf-8')
        error_message = output.stderr
        self.assertEqual(error_message, '実行時にcsvファイルを指定して下さい。\n')

    # 指定されたcsvファイルが2つ以上の場合
    def test_multi_file(self):
        command = ['python3', 'step2_pymee.py',
                   'test/input_file/file1.csv',
                   'test/input_file/file2.csv']

        output = subprocess.run(command,
                                capture_output = True,
                                encoding = 'utf-8')
        error_message = output.stderr

        self.assertEqual(error_message, '指定可能なcsvファイルは1つだけです。\n')

    # 指定されたcsvファイルが存在しない場合
    def test_none_file(self):
        command = ['python3', 'step2_pymee.py',
                   'test/input_file/test999.csv']

        output = subprocess.run(command,
                            capture_output = True,
                            encoding = 'utf-8')
        error_message = output.stderr

        self.assertEqual(error_message, '指定されたcsvファイルは存在しません。\n')

    # 指定されたcsvファイルが空だった場合
    def test_empty_file(self):
        command = ['python3', 'step2_pymee.py',
                   'test/input_file/test_none.csv']

        output = subprocess.run(command,
                                capture_output = True,
                                encoding = 'utf-8')
        error_message = output.stderr

        self.assertEqual(error_message, '指定されたcsvファイルは空です。\n')

# 出力ファイルのテスト
class TestOutputFile(unittest.TestCase):
    # 出力ファイルが存在している場合
    def test_0_exist_output_file(self):
        command = ['python3', 'step2_pymee.py',
                    'test/input_file/test.csv']

        temp_output_file = 'command_ip1.txt'

        # テスト用の一時ファイル作成
        with open(temp_output_file, 'w') as f:
            f.write('test_file')

        output = subprocess.run(command,
                                capture_output = True,
                                encoding = 'utf-8')
        error_message = output.stderr

        self.assertEqual(error_message,
                    f'同名の出力ファイル({temp_output_file})が存在しています。\n')

        # 一時ファイルを削除
        os.unlink(temp_output_file)

    # 処理が正常に終わった場合
    def test_1_output_file(self):
        command = command = ['python3', 'step2_pymee.py',
                             'test/input_file/test.csv']

        output = subprocess.run(command,
                                capture_output = True,
                                encoding = 'utf-8')

        self.assertTrue(filecmp.cmp('command_ip1.txt',
                                'test/result/command_ip1.txt'))
        self.assertTrue(filecmp.cmp('command_ip2.txt',
                                'test/result/command_ip2.txt'))

# 正常処理の確認
class TestNormal(unittest.TestCase):
    def test_fin(self):
        command = command = ['python3', 'step2_pymee.py',
                             'test/input_file/test.csv']

        output = subprocess.run(command,
                                capture_output = True,
                                encoding = 'utf-8')
        fin_message = output.stdout

        self.assertEqual(fin_message, '処理が正常に完了しました。\n')

if __name__ == '__main__':
    # 出力ファイルがある場合は削除する
    output_files = ['command_ip1.txt', 'command_ip2.txt']
    for file in output_files:
        if os.path.exists(file):
            os.unlink(file)
    unittest.main()
