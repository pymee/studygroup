from datetime import datetime
import os
import sys


class SaveTextFile(object):
    __save_path = ""
    __save_filename = ""
    __save_folder = "./results/"

    def __init__(self):
        # 出力するファイル名の生成
        self.__save_filename = "out_{}.txt".format(datetime.now().strftime("%Y%m%d%H%M"))
        self.__save_path = self.__save_folder + self.__save_filename

        # 出力用フォルダとファイルがあるかチェック
        self.check_folder()
        self.check_file()

    def check_folder(self):
        if not os.path.exists(self.__save_folder):
            os.mkdir(self.__save_folder)

    def check_file(self):
        try:
            if os.path.isfile(self.__save_path):
                raise FileExistsError("ファイルが既に存在しています。")
        except FileExistsError:
            print("ファイル名 [{}] は重複しています。".format(self.__save_filename), file=sys.stderr)
            sys.exit(1)

    def save_file(self, write_text):
        with open(self.__save_path, "a", encoding="utf-8") as f:
            f.write(write_text)
        print("保存完了！")


if __name__ == "__main__":
    save_txt_file = SaveTextFile()
    save_txt_file.save_file(["ABC", "DWWF", "FNENF"])
