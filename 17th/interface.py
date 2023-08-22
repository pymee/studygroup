#!/usr/bin/python3

# 1.OpenPyXLライブラリのインポート
import openpyxl

# 2.エクセルのファイルとシートを指定してファイルを開く
# エクセルファイルのパスとシート名
file_path = "linux_config.xlsx"
sheet_name = "interface"

# エクセルファイルを開く
workbook = openpyxl.load_workbook(file_path)
sheet = workbook[sheet_name]

# 3.読み込んだセルを格納する配列の定義
# インターフェースとIPアドレスを格納するリスト
interfaces = []
ipaddresses = []
dg = []
bootprots = []
autoconnects = []

# 4.セルの値を読み込み配列に格納
# B列3行目からセルの値がなくなるまで取得
row = 3
while True:
    interface = sheet["B" + str(row)].value
    if interface is None:
        break
    interfaces.append(interface)

    ipaddress = sheet["C" + str(row)].value
    ipaddresses.append(ipaddress)

    default_gateway = sheet["D" + str(row)].value
    dg.append(default_gateway)

    bootprot = sheet["E" + str(row)].value
    bootprots.append(bootprot)

    autoconnect = sheet["F" + str(row)].value
    autoconnects.append(autoconnect)

    row += 1


# 5.配列に格納した値を使いpythonスクリプトファイルの作成
# Pythonスクリプトファイルを作成してコマンドを出力
with open("configure_interfaces.py", "w") as f:
    f.write("#!/usr/bin/python3\n\n")
    f.write("import subprocess\n\n")
    f.write("# インターフェースとIPアドレスの設定\n")
    for interface, ipaddress, default_gateway, bootprot, autoconnect in zip(interfaces, ipaddresses, dg, bootprots, autoconnects):
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.address', '{ipaddress}'])\n")
        if default_gateway:
            f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.gateway', '{default_gateway}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.method', '{bootprot}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'connection.autoconnect', '{autoconnect}'])\n")

    f.write("# NetworkManagerのサービス再起動\n")
    f.write("subprocess.run(['systemctl', 'restart', 'NetworkManager'])\n\n")

    f.write("# インターフェースの再起動\n")
    for interface in interfaces:
        f.write(f"subprocess.run(['nmcli', 'connection', 'down', '{interface}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'up', '{interface}'])\n")

    f.close()

# エクセルファイルを閉じる
workbook.close()
