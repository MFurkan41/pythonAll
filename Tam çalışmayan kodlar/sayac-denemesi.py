from PyQt5 import QtWidgets
import sys
import time
class Jitter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.say = 0
        self.deger = 1
        self.click = QtWidgets.QPushButton("Tıkla")
        self.saniye_alani = QtWidgets.QLabel("Kalan Saniye: {}".format(10))


        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.saniye_alani)
        self.h_box.addWidget(self.click)
        self.h_box.addStretch()
        self.click.clicked.connect(self.buton)

        self.setLayout(self.h_box)
        self.show()
    def buton(self):
        self.say += 1
        self.click.setText("{}".format(self.say))
        if self.deger == 1:
            for i in range(10, -1, -1):
                time.sleep(1)
                self.saniye_alani.setText(("Kalan Saniye: {}".format(i)))
        self.deger=0
app = QtWidgets.QApplication(sys.argv)

game = Jitter()

sys.exit(app.exec_())