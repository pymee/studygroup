import sys

from PyQt5.QtWidgets import (QLabel, QRadioButton,
                             QPushButton, QVBoxLayout,
                             QHBoxLayout, QApplication,
                             QWidget, QButtonGroup,
                             QMessageBox)

import main

#GUIの環境作成
class MailTest(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
#ラベルとラジオボタンの作成
        self.label1 = QLabel("添付ファイルは必要ですか？")
        self.attach1 = QRadioButton("要")
        self.attach2 = QRadioButton("不要")

#ラジオボタンをグループ化
        self.attach_group1 = QButtonGroup()
        self.attach_group1.addButton(self.attach1)
        self.attach_group1.addButton(self.attach2)

        self.attach1.toggled.connect(self.onClickMail)
        self.attach2.toggled.connect(self.onClickMail)

#メール作成ボタンを作成、「要」「不要」のボタンを押さない限り無効状態にする
        self.buttonA = QPushButton("メール作成", self)
        self.buttonA.setEnabled(False)
        self.buttonA.clicked.connect(self.mail_create)
        self.buttonB = QPushButton("キャンセル", self)
        self.buttonB.clicked.connect(self.mail_cansel)

#ＧＵＩのレイアウトを決める
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.attach1)
        h_layout.addWidget(self.attach2)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label1)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.buttonA)
        v_layout.addWidget(self.buttonB)

        self.setLayout(v_layout)

        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle("メール作成ツール")

        self.show()

#ラジオボタンを選んだ時の動作
    def onClickMail(self):
        radioAttach = self.sender()
        if radioAttach.isChecked():
            if radioAttach == self.attach1:
                self.checkAtt = 0
                self.buttonA.setEnabled(True)
            elif radioAttach == self.attach2:
                self.checkAtt = 1
                self.buttonA.setEnabled(True)

#メール作成のボタンを押した時の動作
    def mail_create(self):
        main.mail_attach_int = self.checkAtt
        main.mailcreate()
        QMessageBox.information(None, "通知", "メール作成が完了しました。", QMessageBox.Yes)
        QApplication.quit()

#キャンセルボタンを押したときの動作
    def mail_cansel(self):
        QMessageBox.information(None, "通知", "メール作成をキャンセルしました。", QMessageBox.Yes)
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MailTest()
    sys.exit(app.exec_())