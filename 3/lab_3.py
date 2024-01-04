from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked1():
    window1.show()

def on_clicked2():
    window2.show()

def on_clicked3():
    window3.show()

def on_clicked4():
    window4.show()

def on_clicked5():
    window5.show()

def on_clicked6():
    window6.show()

app = QtWidgets.QApplication(sys.argv)

# назва групи та роки видання альбомів
window = QtWidgets.QWidget()
window.setWindowTitle("Radiohead 1993-2001")
window.resize(800, 300)

# зображення групи в іконці вікна
ico = QtGui.QIcon('icon.jpg')
app.setWindowIcon(ico)

# зображення назви групи у головному вікні
image_label = QtWidgets.QLabel()
image = QtGui.QPixmap('radiohead.jpg')
image_label.setPixmap(image)

# назва альбому та рік його видання у заголовку вікна
window1 = QtWidgets.QWidget()
window1.setWindowTitle("Pablo Honey (1993)")
ico1 = QtGui.QIcon('pic1.jpg')
window1.setWindowIcon(ico1)
window1.resize(300, 300)

# зображення обкладинки альбому в якості фона
pal_1 = window1.palette()
pal_1.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic1.jpg")))
window1.setPalette(pal_1)

# кнопка з назвою альбому та року його видання
button1 = QtWidgets.QPushButton('Pablo Honey (1993)')
button1.clicked.connect(on_clicked1)

# назва альбому та рік його видання у заголовку вікна
window2 = QtWidgets.QWidget()
window2.setWindowTitle("The Bends (1995)")
window2.resize(300, 300)
ico2 = QtGui.QIcon('pic2.jpg')
window2.setWindowIcon(ico2)

# зображення обкладинки альбому в якості фона
pal_2 = window1.palette()
pal_2.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic2.jpg")))
window2.setPalette(pal_2)

# кнопка з назвою альбому та року його видання
button2 = QtWidgets.QPushButton("The Bends (1995)")
button2.clicked.connect(on_clicked2)

# назва альбому та рік його видання у заголовку вікна
window3 = QtWidgets.QWidget()
window3.setWindowTitle("OK Computer (1997)")
window3.resize(300, 300)
ico3 = QtGui.QIcon('pic3.jpg')
window3.setWindowIcon(ico3)

# зображення обкладинки альбому в якості фона
pal_3 = window1.palette()
pal_3.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic3.jpg")))
window3.setPalette(pal_3)

# кнопка з назвою альбому та року його видання
button3 = QtWidgets.QPushButton("OK Computer (1997)")
button3.clicked.connect(on_clicked3)

# назва альбому та рік його видання у заголовку вікна
window4 = QtWidgets.QWidget()
window4.setWindowTitle("Kid A (2000)")
window4.resize(300, 300)
ico4 = QtGui.QIcon('pic4.jpg')
window4.setWindowIcon(ico4)

# зображення обкладинки альбому в якості фона
pal_4 = window1.palette()
pal_4.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic4.jpg")))
window4.setPalette(pal_4)

# кнопка з назвою альбому та року його видання
button4 = QtWidgets.QPushButton("Kid A (2000)")
button4.clicked.connect(on_clicked4)

# назва альбому та рік його видання у заголовку вікна
window5 = QtWidgets.QWidget()
window5.setWindowTitle("Amnesiac (2001)")
window5.resize(300, 300)
ico5 = QtGui.QIcon('pic5.jpg')
window5.setWindowIcon(ico5)

# зображення обкладинки альбому в якості фона
pal_5 = window1.palette()
pal_5.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic5.jpg")))
window5.setPalette(pal_5)

# кнопка з назвою альбому та року його видання
button5 = QtWidgets.QPushButton("Amnesiac (2001)")
button5.clicked.connect(on_clicked5)

# назва альбому та рік його видання у заголовку вікна
window6 = QtWidgets.QWidget()
window6.setWindowTitle("I might be wrong (2001)")
window6.resize(300, 300)
ico6 = QtGui.QIcon('pic6.jpg')
window6.setWindowIcon(ico6)

# зображення обкладинки альбому в якості фона
pal_6 = window1.palette()
pal_6.setBrush(QtGui.QPalette.ColorGroup.Normal,
             QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(QtGui.QPixmap("pic6.jpg")))
window6.setPalette(pal_6)

# кнопка з назвою альбому та року його видання
button6 = QtWidgets.QPushButton("I might be wrong (2001)")
button6.clicked.connect(on_clicked6)

hbox1 = QtWidgets.QHBoxLayout()
hbox1.addWidget(button1)
hbox1.addWidget(button2)

hbox2 = QtWidgets.QHBoxLayout()
hbox2.addWidget(button3)
hbox2.addWidget(button4)

hbox3 = QtWidgets.QHBoxLayout()
hbox3.addWidget(button5)
hbox3.addWidget(button6)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(image_label)
vbox.addLayout(hbox1)
vbox.addLayout(hbox2)
vbox.addLayout(hbox3)

window.setLayout(vbox)

window.show()
sys.exit(app.exec())
