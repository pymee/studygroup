from datetime import datetime
import string


class OutPutTextCreator(object):
    __ipaddr = ""
    __username = ""
    __command = ""

    def __init__(self):
        # 最初に出力用テンプレートを読み込んでプロパティに代入しておけば今後余計なIO減らせそう
        with open('./templates/result_content.txt', 'r') as f:
            self.__template = string.Template(f.read())

    def set_remote_info(self, ipaddr, username, command):
        # IPアドレス変わったときにインスタンスにセットし直す
        self.__ipaddr = ipaddr
        self.__username = username
        self.__command = command

    def replace_content(self, stdout_list):
        # stringライブラリを使って出力用のテキストを生成する
        t = self.__template

        command_rst = ""
        for i in stdout_list:
            command_rst += i + "\n"

        content = t.substitute(ipaddr=self.__ipaddr, username=self.__username, nowtime=datetime.now().strftime("%H:%M"),
                               command=self.__command, command_result=command_rst)

        return content


if __name__ == "__main__":
    optc = OutPutTextCreator("192.168.0.1", "nelsia", "ls", ["100", "/home/user", "hogehoge"])
