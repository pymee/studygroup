import paramiko
import sys


class SSHConnector(object):
    __hostname = ""
    __username = ""
    __password = ""
    __port = ""
    __ssh = None

    def __init__(self, hostname, username, password, port=22):
        """
        インスタンス生成時に以下のパラメータをフィールドにセット
        :param hostname:
        :param username:
        :param password:
        :param port:
        """
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__port = port
        self.init_ssh()

    def __del__(self):
        self.__ssh.close()

    def init_ssh(self):
        try:
            self.__ssh = paramiko.SSHClient()
            self.__ssh.load_system_host_keys()
            self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.__ssh.connect(hostname=self.__hostname, username=self.__username, password=self.__password,
                               port=self.__port, timeout=15.0, look_for_keys=False)
        except paramiko.ssh_exception.AuthenticationException as e:
            print(e, file=sys.stderr)
            sys.exit(1)

    @staticmethod
    def format_stdout(stdout):
        stdout_list = [i.strip("\n") for i in stdout]

        return stdout_list

    def send_command(self, command):
        stdin, stdout, stderr = self.__ssh.exec_command(command)

        return self.format_stdout(stdout)
