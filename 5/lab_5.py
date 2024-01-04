from PyQt6 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)

# назва групи у заголовку вікна
window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein Discography 1995-2004")
window.resize(1000, 450)

# зображення групи в іконці вікна
ico = QtGui.QIcon('../6/ico.png')
app.setWindowIcon(ico)

# назва групи
name_label = QtWidgets.QLabel('Rammstein')
name_label.setFont(QtGui.QFont('Arial Black', 20))
name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
name_label.setStyleSheet('font-weight: bold;\
                         background-color: black;\
                         color: white')

# зображення групи
image_label = QtWidgets.QLabel()
image = QtGui.QPixmap('ramm.jpg')
image_label.setPixmap(image)

info_label = QtWidgets.QLabel('Discography 1995-2004')
info_label.setFont(QtGui.QFont('Arial Black', 20))
info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
info_label.setStyleSheet('font-weight: bold;\
                         background-color: black;\
                         color: white')

# інформація про дискографію групи
disco_1995 = QtWidgets.QLabel("Herzeleid (album) \nDu riechst so gut (single)")
disco_1995.setFont(QtGui.QFont('Arial Black', 16))

disco_1997 = QtWidgets.QLabel("Sehnsucht (album) \nDu hast (single) \nDas Modell (single)")
disco_1997.setFont(QtGui.QFont('Arial Black', 16))

disco_2001 = QtWidgets.QLabel("Mutter (album) \nAsche zu Asche (single) \nSonne (single) \nLinks 2 3 4 (single) \nIch will (single)")
disco_2001.setFont(QtGui.QFont('Arial Black', 16))

disco_2004 = QtWidgets.QLabel('Reise, Reise (album) \nMein Teil (single) \nAmerika (single) \nOhne dich (single)')
disco_2004.setFont(QtGui.QFont('Arial Black', 16))

disco_2005 = QtWidgets.QLabel('Rosenrot (album) \nKeine Lust (single) \nBenzin (single) \nRosenrot (single)')
disco_2005.setFont(QtGui.QFont('Arial Black', 16))

toolBox = QtWidgets.QToolBox()
toolBox.addItem(disco_1995, '1995')
toolBox.addItem(disco_1997, '1997')
toolBox.addItem(disco_2001, '2001')
toolBox.addItem(disco_2004, '2004')
toolBox.addItem(disco_2005, '2005')

font = QtGui.QFont('Arial Black', 18)
font.setBold(True)
toolBox.setFont(font)

vbox1 = QtWidgets.QVBoxLayout()
vbox1.addWidget(name_label)
vbox1.addWidget(image_label)

vbox2 = QtWidgets.QVBoxLayout()
vbox2.addWidget(info_label)
vbox2.addWidget(toolBox)

hbox = QtWidgets.QHBoxLayout()
hbox.addLayout(vbox1)
hbox.addLayout(vbox2)

window.setLayout(hbox)

window.show()
sys.exit(app.exec())

