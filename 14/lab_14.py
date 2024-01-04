from PyQt6 import QtCore, QtWidgets, QtGui
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Rammstein")
        ico = QtGui.QIcon('ico.png')
        self.setWindowIcon(ico)
        self.settings = QtCore.QSettings("Rammstein",
                                         "Mutter Album")
        vbox = QtWidgets.QVBoxLayout()
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.ColorGroup.Normal,
                     QtGui.QPalette.ColorRole.Window,
                     QtGui.QBrush(QtGui.QPixmap("album_mutter.jpg")))
        self.setPalette(pal)
        self.setLayout(vbox)

        if self.settings.contains("MyWindow/Location"):
            self.setGeometry(self.settings.value("MyWindow/Location"))
        else:
            self.resize(300, 300)

    def closeEvent(self, evt):
        self.settings.beginGroup("MyWindow")
        self.settings.setValue("Location", self.geometry())
        self.settings.endGroup()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
