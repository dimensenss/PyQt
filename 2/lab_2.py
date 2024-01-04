from PyQt6 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Slipknot")
window.resize(600, 493)

ico = QtGui.QIcon('album.jpg')
window.setWindowIcon(ico)

pal = window.palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("slipknot.jpg")))
window.setPalette(pal)

lbl_1 = QtWidgets.QLabel('And the rain will kill us all')
lbl_1.setStyleSheet('color: red; font-style: italic')
lbl_2 = QtWidgets.QLabel('Throw ourselves against the wall')
lbl_2.setStyleSheet('color: white; font-style: italic')
lbl_3 = QtWidgets.QLabel('But no one else can see')
lbl_3.setStyleSheet('color: red; font-style: italic')
lbl_4 = QtWidgets.QLabel('The preservation of the martyr in me')
lbl_4.setStyleSheet('color: white; font-style: italic')


box = QtWidgets.QGroupBox('Psychosocial')
box.setStyleSheet('color: white; font-weight: bold; font-size: 18px')
bbox = QtWidgets.QVBoxLayout()
bbox.addWidget(lbl_1)
bbox.addWidget(lbl_2)
bbox.addWidget(lbl_3)
bbox.addWidget(lbl_4)
box.setLayout(bbox)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(box)
window.setLayout(vbox)

window.show()
sys.exit(app.exec())
