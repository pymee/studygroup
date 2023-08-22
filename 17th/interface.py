#!/usr/bin/python3

# 1.OpenPyXL���C�u�����̃C���|�[�g
import openpyxl

# 2.�G�N�Z���̃t�@�C���ƃV�[�g���w�肵�ăt�@�C�����J��
# �G�N�Z���t�@�C���̃p�X�ƃV�[�g��
file_path = "linux_config.xlsx"
sheet_name = "interface"

# �G�N�Z���t�@�C�����J��
workbook = openpyxl.load_workbook(file_path)
sheet = workbook[sheet_name]

# 3.�ǂݍ��񂾃Z�����i�[����z��̒�`
# �C���^�[�t�F�[�X��IP�A�h���X���i�[���郊�X�g
interfaces = []
ipaddresses = []
dg = []
bootprots = []
autoconnects = []

# 4.�Z���̒l��ǂݍ��ݔz��Ɋi�[
# B��3�s�ڂ���Z���̒l���Ȃ��Ȃ�܂Ŏ擾
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


# 5.�z��Ɋi�[�����l���g��python�X�N���v�g�t�@�C���̍쐬
# Python�X�N���v�g�t�@�C�����쐬���ăR�}���h���o��
with open("configure_interfaces.py", "w") as f:
    f.write("#!/usr/bin/python3\n\n")
    f.write("import subprocess\n\n")
    f.write("# �C���^�[�t�F�[�X��IP�A�h���X�̐ݒ�\n")
    for interface, ipaddress, default_gateway, bootprot, autoconnect in zip(interfaces, ipaddresses, dg, bootprots, autoconnects):
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.address', '{ipaddress}'])\n")
        if default_gateway:
            f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.gateway', '{default_gateway}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'ipv4.method', '{bootprot}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'modify', '{interface}', 'connection.autoconnect', '{autoconnect}'])\n")

    f.write("# NetworkManager�̃T�[�r�X�ċN��\n")
    f.write("subprocess.run(['systemctl', 'restart', 'NetworkManager'])\n\n")

    f.write("# �C���^�[�t�F�[�X�̍ċN��\n")
    for interface in interfaces:
        f.write(f"subprocess.run(['nmcli', 'connection', 'down', '{interface}'])\n")
        f.write(f"subprocess.run(['nmcli', 'connection', 'up', '{interface}'])\n")

    f.close()

# �G�N�Z���t�@�C�������
workbook.close()
