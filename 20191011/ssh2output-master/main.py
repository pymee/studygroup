#!/usr/bin/env python3

from libs.myParser import parser
import exec_command
from libs.SaveTextFile import SaveTextFile


def main():
    # コマンドライン引数チェック(libsフォルダのmyParser.pyファイルを使用)
    args = parser()

    # CSVファイルを読み込んで、コマンドを実行後に保存用テキストに変換(面倒だからこのメソッドでほとんどやってしまった)
    save_text = exec_command.exec_command(args)

    # resultsフォルダに保存
    save_txt_file = SaveTextFile()
    save_txt_file.save_file(save_text)


if __name__ == '__main__':
    main()
