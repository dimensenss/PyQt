from PyQt6 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")  # Використовуємо стиль Fusion для темної теми

# назва групи та роки видання альбомів
window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein")
window.resize(900, 600)

# зображення групи в іконці вікна
ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)

# зображення обкладинок альбомів
image_1 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_6.jpg')
image_1.setPixmap(image)

image_2 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_1.png')
image_2.setPixmap(image)

image_3 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_2.jpg')
image_3.setPixmap(image)

image_4 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_3.jpg')
image_4.setPixmap(image)

image_5 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_4.jpg')
image_5.setPixmap(image)

image_6 = QtWidgets.QLabel()
image = QtGui.QPixmap('album_5.jpg')
image_6.setPixmap(image)

# горизонтальний контейнер
hbox1 = QtWidgets.QHBoxLayout()
hbox1.addWidget(image_1)
hbox1.addWidget(image_2)
hbox1.addWidget(image_3)

# горизонтальний контейнер
hbox2 = QtWidgets.QHBoxLayout()
hbox2.addWidget(image_4)
hbox2.addWidget(image_5)
hbox2.addWidget(image_6)

# вертикальний контейнер
vbox = QtWidgets.QVBoxLayout()
vbox.addLayout(hbox1)
vbox.addLayout(hbox2)

window.setLayout(vbox)

window.show()
sys.exit(app.exec())
