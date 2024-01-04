from PyQt6 import QtGui, QtWidgets, QtCore
import sys

class ColorDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, colors, parent=None):
        super().__init__(parent)
        self.colors = colors

    def paint(self, painter, option, index):
        painter.fillRect(option.rect, QtGui.QBrush(self.colors[index.column()]))
        super().paint(painter, option, index)

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein Video")
tv = QtWidgets.QTableView(parent=window)
sti = QtGui.QStandardItemModel(parent=window)

ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)

title_list = ['Rammstein - Du Hast', 'Rammstein - Deutschland',
              "Rammstein - Ich Will", "Rammstein - Sonne",
              'Rammstein - Feuer Frei!', 'Rammstein - Keine Lust']

youtube_list = ['https://www.youtube.com/watch?v=W3q8Od5qJio&t=2s',
                'https://www.youtube.com/watch?v=NeQM1c-XCDc',
                'https://www.youtube.com/watch?v=EOnSh3QlpbQ',
                'https://www.youtube.com/watch?v=StZcUAPRRac',
                'https://www.youtube.com/watch?v=ZkW-K5RQdzo',
                'https://www.youtube.com/watch?v=1M4ADcMn3dA']

preview_list = ['video1.jpg', 'video2.jpg', 'video3.jpg',
                'video4.jpg', 'video5.jpg', 'video6.jpg']

colors = [QtGui.QColor("black"), QtGui.QColor("black"), QtGui.QColor("gray")]

for row in range(0, 6):
    item1 = QtGui.QStandardItem(QtGui.QIcon(preview_list[row]), '')
    item2 = QtGui.QStandardItem(title_list[row])
    item3 = QtGui.QStandardItem(youtube_list[row])
    sti.appendRow([item1, item2, item3])

sti.setHorizontalHeaderLabels(['Preview', 'Title', 'YouTube'])
tv.setModel(sti)
for row in range(0, 6):
    tv.setRowHeight(row, 90)

delegate = ColorDelegate(colors)
tv.setItemDelegate(delegate)

# Установка стилей для изменения цвета текста и шрифта
style = """
    QTableView {
        background-color: black;
        color: white;
        font-family: Arial Black;
        font-size: 12px;
    }

    QHeaderView::section {
        background-color: black;
        color: white;
        font-weight: bold;
    }

    QTableView::item:column(2) {
        color: white;
    }
"""

tv.setStyleSheet(style)

tv.setColumnWidth(0, 160)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 300)
tv.setIconSize(QtCore.QSize(160, 90))
tv.resize(630, 570)

window.show()
sys.exit(app.exec())
