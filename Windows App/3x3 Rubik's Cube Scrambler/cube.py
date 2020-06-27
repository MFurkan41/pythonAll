import random
import re
from PyQt5 import QtCore, QtGui, QtWidgets

Notation = ["R", "R'", "L", "L'", "U", "U'", "F", "F'", "B", "B'"]

def Generator(length):
	Scramble = []
	while len(Scramble) < length:
		Move = random.choice(Notation)
		MoveStr = " ".join(re.findall("[a-zA-Z]+", str(Move)))
		PreviousMove = Scramble[-1:]
		PreviousMove = " ".join(re.findall("[a-zA-Z]+", str(PreviousMove)))
		if MoveStr != PreviousMove:
			Num = random.randint(1,3)
			if Num == 1 or Num == 3:
				Scramble.append(Move)
			else:
				if "'" in str(Move):
					Move = str(Move).replace("'", "")
				Scramble.append('{}2'.format(Move))
	T = ""
	for moves in Scramble:
		T = T + " " + str(moves)
	return T

class Ui_Form(object):
    def setupUi(self, Form):
            Form.setWindowTitle("3x3 Cube Scrambler - By M.Furkan YOLAL")
            Form.resize(1700, 300)
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(210, 80, 61, 156))
            font = QtGui.QFont()
            font.setPointSize(140)
            font.setBold(True)
            font.setWeight(150)
            self.label.setFont(font)
            self.label.resize(1600,400)
            self.label.move(60,-75)
            self.label.setFont(QtGui.QFont('Arial', 50))
            self.label.setObjectName("label")
            self.label.setText(Generator(15))
            self.pushButton = QtWidgets.QPushButton(Form)
            self.pushButton.setGeometry(QtCore.QRect(1450, 200, 151, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton.setFont(font)
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setText("Scramble")
            self.pushButton.clicked.connect(self.on_click)
            QtCore.QMetaObject.connectSlotsByName(Form)
    def on_click(self):
        self.label.setText(Generator(15))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

