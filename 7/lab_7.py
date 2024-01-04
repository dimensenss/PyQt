from PyQt6 import QtCore, QtWidgets, QtSql, QtGui
from PyQt6.QtWidgets import QTimeEdit
import sys

# делегат для внесення даних про тривалість пісні
class TimeDelegate(QtSql.QSqlRelationalDelegate):
    def createEditor(self, parent, option, index):
        if index.column() == 2:
            timeEdit = QTimeEdit(parent)
            timeEdit.setDisplayFormat("mm:ss")
            timeEdit.setTime(QtCore.QTime(0, 0))
            return timeEdit
        else:
            return super().createEditor(parent, option, index)

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()

# Назва групи у заголовку вікна
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")  # Використовуємо стиль Fusion для темної теми

dark_palette = QtGui.QPalette()
dark_palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.ColorRole.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.ToolTipText, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.Text, QtCore.Qt.GlobalColor.gray)
dark_palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ColorRole.ButtonText, QtCore.Qt.GlobalColor.black)
dark_palette.setColor(QtGui.QPalette.ColorRole.Highlight, QtGui.QColor(142, 45, 197))
dark_palette.setColor(QtGui.QPalette.ColorRole.HighlightedText, QtCore.Qt.GlobalColor.black)

app.setPalette(dark_palette)

# Зміна шрифту на Arial Black
font = QtGui.QFont("Arial Black", 10)
app.setFont(font)

window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein Songs")

# Зображення групи в іконці вікна
ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)

con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite3')
con.open()

# Створення таблиці для даних про пісні
query = QtSql.QSqlQuery()
query.exec(
    """
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        length TIME,
        album_id INTEGER,
        author TEXT,
        FOREIGN KEY (album_id) REFERENCES albums(id)
    )
    """
)

# Створення таблиці з даними про альбоми
query.exec(
    """
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY,
        albumname TEXT
    )
    """
)

# Внесення назви трьох альбомів
query.exec("SELECT COUNT(*) FROM albums")
query.next()
if query.value(0) == 0:
    query.exec("INSERT INTO albums (albumname) VALUES ('Zeit')")
    query.exec("INSERT INTO albums (albumname) VALUES ('Mutter')")
    query.exec("INSERT INTO albums (albumname) VALUES ('Rammstein')")

stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setTable('songs')
stm.setSort(1, QtCore.Qt.SortOrder.AscendingOrder)
stm.setRelation(3, QtSql.QSqlRelation('albums', 'id', 'albumname'))
stm.select()
stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Song Title')
stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Length')
stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, 'Album Title')
stm.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, 'Author')
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)

# Використання делегата для внесення назв альбомів
tv.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(tv))

# Використання делегата для внесення тривалості пісні
timeDelegate = TimeDelegate(tv)
tv.setItemDelegateForColumn(2, timeDelegate)

tv.hideColumn(0)
tv.setColumnWidth(1, 225)
tv.setColumnWidth(2, 80)
tv.setColumnWidth(3, 140)

vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Додати запис")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Видалити запис")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(510, 250)
window.show()
sys.exit(app.exec())
