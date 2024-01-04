from PyQt6 import QtCore, QtWidgets, QtGui
import sys


# визначення окремих вікон для кожної пісні
class MyWidget_1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel()
        self.label.setText("<b>Die Tränen greiser Kinderschar</b><br><br>"
                            "Ich zieh sie auf ein weißes Haar<br>"
                            "Werf in die Luft die nasse Kette<br>"
                            "Und wünsch mir, dass ich eine Mutter hätte<br>"
                            "Keine Sonne, die mir scheint<br>"
                            "Keine Brust hat Milch geweint<br>"
                            "In meiner Kehle steckt ein Schlauch<br>"
                            "Hab keinen Nabel auf dem Bauch<br>"
                            "Mutter, Mutter<br>"
                            "Mutter, Mutter<br>"
                            "Ich durfte keine Nippel lecken<br>"
                            "Und keine Falte zum Verstecken<br>"
                            "Niemand gab mir einen Namen<br>"
                            "Gezeugt in Hast und ohne Samen<br>"
                            "Der Mutter, die mich nie geboren<br>"
                            "Hab ich heute Nacht geschworen<br>"
                            "Ich werd ihr eine Krankheit schenken<br>"
                            "Und sie danach im Fluss versenken<br>"
                            "Mutter, Mutter<br>"
                            "Mutter, Mutter<br>"
                            "Mutter, Mutter<br>"
                            "Mutter, Mutter<br>"
                            "In ihren Lungen wohnt ein Aal<br>"
                            "Auf meiner Stirn ein Muttermal<br>"
                            "Entferne es mit Messers Kuss<br>"
                            "Auch wenn ich daran sterben muss<br>"
                            "Mutter, Mutter<br>"
                            "Mutter, Mutter<br>"
                            "In ihren Lungen wohnt ein Aal<br>"
                            "Auf meiner Stirn ein Muttermal<br>"
                            "Entferne es mit Messers Kuss<br>"
                            "Auch wenn ich verbluten muss<br>"
                            "Mutter<br>"
                            "Oh gib mir Kraft<br>"
                            "Mutter, Mutter<br>"
                            "Oh gib mir Kraft<br>"
                            "Mutter, Mutter<br>"
                            "Oh gib mir Kraft<br>"
                            "Mutter, Mutter<br>"
                            "Oh gib mir Kraft")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)


class MyWidget_2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel()
        self.label.setText("<b>Wir durften nicht dazugehören</b><br><br>"
                            "Nichts sehen, reden oder hören<br>"
                            "Doch jede Nacht für ein, zwei Stunden<br>"
                            "Bin ich dieser Welt entschwunden<br>"
                            "Jede Nacht ein bisschen froh<br>"
                            "Mein Ohr ganz nah am Weltempfänger<br>"
                            "Radio, mein Radio<br>"
                            "Ich lass mich in den Äther saugen<br>"
                            "Meine Ohren werden Augen<br>"
                            "Radio, mein Radio<br>"
                            "So höre ich, was ich nicht seh<br>"
                            "Stille heimlich fernes Weh<br>"
                            "Wir durften nicht dazugehören<br>"
                            "Nichts sehen, reden oder stören<br>"
                            "Jenes Liedgut war verboten<br>"
                            "So gefährlich fremde Noten<br>"
                            "Doch jede Nacht ein wenig froh<br>"
                            "Mein Ohr ganz nah am Weltempfänger<br>"
                            "Radio, mein Radio<br>"
                            "Ich lass mich in den Äther saugen<br>"
                            "Meine Ohren werden Augen<br>"
                            "Radio, mein Radio<br>"
                            "So höre ich, was ich nicht seh<br>"
                            "Stille heimlich fernes Weh<br>"
                            "Jede Nacht ich heimlich stieg<br>"
                            "Auf den Rücken der Musik<br>"
                            "Leg die Ohren an die Schwingen<br>"
                            "Leise in die Hände singen<br>"
                            "Jede Nacht und wieder flieg<br>"
                            "Ich einfach fort mit der Musik<br>"
                            "Schwebe so durch alle Räume<br>"
                            "Keine Grenzen, keine Zäune<br>"
                            "Radio, mein Radio<br>"
                            "Radio, mein Radio<br>"
                            "Radio, mein Radio<br>"
                            "Ich lass mich in den Äther saugen<br>"
                            "Meine Ohren werden Augen<br>"
                            "Radio, mein Radio<br>"
                            "So höre ich, was ich nicht seh<br>"
                            "Stille heimlich fernes Weh")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)


class MyWidget_3(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel()
        self.label.setText("<b>Wenn die Kinder unerzogen</b><br><br>"
                            "Schon der Vater hat gedroht<br>"
                            "Der schwarze Mann, er wird dich holen<br>"
                            "Wenn du nicht folgst meinem Gebot<br>"
                            "Und das glauben wir bis heute<br>"
                            "So in Angst sind Land und Leute<br>"
                            "Etwas Schlimmes wird geschehen<br>"
                            "Das Böse kommt, wird nicht mehr gehen<br>"
                            "Und die Furcht wächst in die Nacht<br>"
                            "Tür und Tore sind bewacht<br>"
                            "Die Rücken nass, die Hände klamm<br>"
                            "Alle haben Angst vorm schwarzen Mann<br>"
                            "In Dunkelheit schleicht er heran<br>"
                            "Bist du nicht brav, fasst er dich an<br>"
                            "Traue keinem Fremden dann<br>"
                            "So viel Albtraum, so viel Wahn<br>"
                            "Und so glauben wir bis heute<br>"
                            "Schwer bewaffnet ist die Meute<br>"
                            "Ach, sie können es nicht lassen<br>"
                            "Schreien Feuer in die Gassen<br>"
                            "Und die Furcht wächst in die Nacht<br>"
                            "Gar kein Auge zugemacht<br>"
                            "Der Rücken nass, die Hände klamm<br>"
                            "Alle haben Angst vorm schwarzen Mann<br>"
                            "Wer hat Angst vorm schwarzen Mann?<br>"
                            "Wer hat Angst vorm schwarzen Mann?<br>"
                            "Wer hat Angst vorm schwarzen Mann?<br>"
                            "Wer hat Angst?<br>"
                            "Und die Furcht wächst in die Nacht<br>"
                            "Gar kein Auge zugemacht<br>"
                            "Die Rücken nass, die Hände klamm<br>"
                            "Alle haben Angst<br>"
                            "Schwarzer Mann<br>"
                            "Schwarzer Mann")

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)


# визначення головного вікна
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.mdi_area = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.add_menu()

    # визначення головного меню
    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("Songs")

        self.actCreate_1 = QtGui.QAction("Mutter", None)
        self.actCreate_1.triggered.connect(self.on_create_sub_window_1)
        self.menuFile.addAction(self.actCreate_1)

        self.actCreate_2 = QtGui.QAction("Radio", None)
        self.actCreate_2.triggered.connect(self.on_create_sub_window_2)
        self.menuFile.addAction(self.actCreate_2)

        self.actCreate_3 = QtGui.QAction("Angst", None)
        self.actCreate_3.triggered.connect(self.on_create_sub_window_3)
        self.menuFile.addAction(self.actCreate_3)

        self.menuBar().addMenu(self.menuFile)

        self.menuWindow = QtWidgets.QMenu("&Window")
        self.actCascade = QtGui.QAction("Casca&de", None)
        self.actCascade.triggered.connect(
            self.mdi_area.cascadeSubWindows)
        self.menuWindow.addAction(self.actCascade)

        self.actTile = QtGui.QAction("&Tile", None)
        self.actTile.triggered.connect(
            self.mdi_area.tileSubWindows)
        self.menuWindow.addAction(self.actTile)

        self.actCloseActive = QtGui.QAction("CloseActi&ve", None)
        self.actCloseActive.triggered.connect(
            self.mdi_area.closeActiveSubWindow)
        self.menuWindow.addAction(self.actCloseActive)

        self.actCloseAll = QtGui.QAction("Close&All", None)
        self.actCloseAll.triggered.connect(
            self.mdi_area.closeAllSubWindows)
        self.menuWindow.addAction(self.actCloseAll)

        self.menuBar().addMenu(self.menuWindow)

    # відображення текстів пісень в окремих вікнах
    def on_create_sub_window_1(self):
        ico = QtGui.QIcon('album_mutter.jpg')
        w = MyWidget_1()
        sWindow = self.mdi_area.addSubWindow(w)
        sWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        sWindow.resize(300, 440)
        sWindow.setWindowIcon(ico)
        sWindow.setWindowTitle("Mutter")
        sWindow.show()

    def on_create_sub_window_2(self):
        ico = QtGui.QIcon('album_ramm.png')
        w = MyWidget_2()
        sWindow = self.mdi_area.addSubWindow(w)
        sWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        sWindow.resize(300, 430)
        sWindow.setWindowIcon(ico)
        sWindow.setWindowTitle("Rammstein")
        sWindow.show()

    def on_create_sub_window_3(self):
        ico = QtGui.QIcon('album_zeit.png')
        w = MyWidget_3()
        sWindow = self.mdi_area.addSubWindow(w)
        sWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        sWindow.resize(300, 530)
        sWindow.setWindowIcon(ico)
        sWindow.setWindowTitle("Zeit")
        sWindow.show()


app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")  # Використовуємо стиль Fusion для темної теми

dark_palette = QtGui.QPalette()
dark_palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Text, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(142, 45, 197))
dark_palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtCore.Qt.GlobalColor.black)

app.setPalette(dark_palette)

# Зміна шрифту на Arial Black
font = QtGui.QFont("Arial Black", 10)
app.setFont(font)
window = MyWindow()
# назва групи у заголовку вікна
window.setWindowTitle("Rammstein Songs")
# зображення групи в іконці вікна
ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)
window.resize(940, 550)
window.show()
sys.exit(app.exec())
