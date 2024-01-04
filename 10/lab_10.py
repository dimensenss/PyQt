from PyQt6 import QtWidgets, QtGui,QtCore
import sys

# створення діалогового вікна
def on_clicked_1():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Тілль Лі́ндеманн</b><br>4 січня 1963")
    dialog.setInformativeText("Лейпциг,<b> НДР</b>")
    dialog.setDetailedText('Німецький вокаліст, автор текстів пісень і фронтмен'
                           ' метал-груп Rammstein, Lindemann і Na Chui, поет. ')
    result = dialog.exec()

# створення діалогового вікна
def on_clicked_2():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Крістіан Лоренц</b><br>16 листопада 1966")
    dialog.setInformativeText("Східний Берлін,<b> НДР</b>")
    dialog.setDetailedText(
        'Німецький музикант, найбільш відомий як клавішник '
        'німецької індастріал-метал групи Rammstein.')
    result = dialog.exec()

def on_clicked_3():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Крістоф Шнайдер</b><br> 11 травня 1966")
    dialog.setInformativeText("Східний Берлін, <b>НДР</b>")
    dialog.setDetailedText('Німецький рок-музикант, на прізвисько «Doom», '
                           'найбільш відомий як барабанщик '
                           'індастріал-метал групи Rammstein.')
    result = dialog.exec()

def on_clicked_4():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Олівер Рідель</b><br> 11 квітня 1971")
    dialog.setInformativeText("Шверін, <b>НДР</b>")
    dialog.setDetailedText('Hімецький музикант, найбільш відомий як '
                           'бас-гітарист німецького гурту Rammstein.')
    result = dialog.exec()

def on_clicked_5():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Пауль Ландерс</b><br> 9 грудня 1964")
    dialog.setInformativeText("Східний Берлін, <b>НДР</b>")
    dialog.setDetailedText('Німецький музикант, ритм-гітарист групи Rammstein. '
                           'Раніше він належав до фанатської групи НДР Feeling B,'
                           ' яка вплинула на альтернативну музичну сцену НДР.')
    result = dialog.exec()

def on_clicked_6():
    dialog = QtWidgets.QMessageBox(parent=window)
    dialog.setWindowTitle("Personal Information")
    dialog.setText("Народився <b>Ріхард Круспе</b><br> 24 червня 1967")
    dialog.setInformativeText("Віттенберге, <b>НДР</b>")
    dialog.setDetailedText('Німецький музикант, найбільш відомий як гітарист '
                           'і співзасновник німецької індастріал групи '
                           'Rammstein та лідер проекту Emigrate.')
    result = dialog.exec()

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")  # Використовуємо стиль Fusion для темної теми

dark_palette = QtGui.QPalette()
dark_palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.Text, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtCore.Qt.GlobalColor.white)
dark_palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(142, 45, 197))
dark_palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtCore.Qt.GlobalColor.black)

app.setPalette(dark_palette)
# назва групи у заголовку вікна
window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein group")
window.resize(300, 500)

# зображення групи в іконці вікна
ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)

# зображення виконавців
image_1 = QtWidgets.QLabel()
image = QtGui.QPixmap('Till.jpg')
image_1.setPixmap(image)

image_2 = QtWidgets.QLabel()
image = QtGui.QPixmap('Chrisitan.jpg')
image_2.setPixmap(image)

image_3 = QtWidgets.QLabel()
image = QtGui.QPixmap('Christoph.jpg')
image_3.setPixmap(image)

image_4 = QtWidgets.QLabel()
image = QtGui.QPixmap('Oliver.jpg')
image_4.setPixmap(image)

image_5 = QtWidgets.QLabel()
image = QtGui.QPixmap('Paul.jpg')
image_5.setPixmap(image)

image_6 = QtWidgets.QLabel()
image = QtGui.QPixmap('richard.jpg')
image_6.setPixmap(image)

# горизонтальний контейнер
hbox1 = QtWidgets.QHBoxLayout()
hbox3 = QtWidgets.QHBoxLayout()
hbox1.addWidget(image_1)
hbox1.addWidget(image_2)
hbox1.addWidget(image_3)
hbox3.addWidget(image_4)
hbox3.addWidget(image_5)
hbox3.addWidget(image_6)

# кнопки з іменами виконавців
button_1 = QtWidgets.QPushButton("Till Lindemann")
button_1.clicked.connect(on_clicked_1)
button_2 = QtWidgets.QPushButton("Christian Lorenz")
button_2.clicked.connect(on_clicked_2)
button_3 = QtWidgets.QPushButton("Christoph Schneider")
button_3.clicked.connect(on_clicked_3)
button_4 = QtWidgets.QPushButton("Oliver Riedel")
button_4.clicked.connect(on_clicked_4)
button_5 = QtWidgets.QPushButton("Paul Landers")
button_5.clicked.connect(on_clicked_5)
button_6 = QtWidgets.QPushButton("Richard Kruspe")
button_6.clicked.connect(on_clicked_6)

# горизонтальний контейнер
hbox2 = QtWidgets.QHBoxLayout()
hbox5 = QtWidgets.QHBoxLayout()
hbox2.addWidget(button_1)
hbox2.addWidget(button_2)
hbox2.addWidget(button_3)
hbox5.addWidget(button_4)
hbox5.addWidget(button_5)
hbox5.addWidget(button_6)

# вертикальний контейнер
vbox = QtWidgets.QVBoxLayout()
vbox.addLayout(hbox1)
vbox.addLayout(hbox2)
vbox.addLayout(hbox3)
vbox.addLayout(hbox5)



window.setLayout(vbox)
window.show()

sys.exit(app.exec())
