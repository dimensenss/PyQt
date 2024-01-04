import sys

from PyQt6 import QtCore, QtWidgets, QtSql, QtGui
from PyQt6.QtWidgets import QTimeEdit

class TimeDelegate(QtSql.QSqlRelationalDelegate):
    def createEditor(self, parent, option, index):
        if index.column() == 1:
            timeEdit = QTimeEdit(parent)
            timeEdit.setDisplayFormat("hh:mm")
            timeEdit.setTime(QtCore.QTime(0, 0))
            return timeEdit
        else:
            return super().createEditor(parent, option, index)

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()

if __name__ == "__main__":
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
    window = QtWidgets.QWidget()
    window.setWindowTitle("Diary")

    ico = QtGui.QIcon('icon.png')
    app.setWindowIcon(ico)

    con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName('data.sqlite3')
    con.open()

    query = QtSql.QSqlQuery()

    query.exec(
        """
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY,
            action_time TIME,
            action_name TEXT,
            importance_id INTEGER,
            urgency_id INTEGER,
            status_id INTEGER,
            FOREIGN KEY (importance_id) REFERENCES importance(id),
            FOREIGN KEY (urgency_id) REFERENCES urgency(id),
            FOREIGN KEY (status_id) REFERENCES status(id)
        )
        """
    )

    query.exec(
        """
        CREATE TABLE IF NOT EXISTS importance (
            id INTEGER PRIMARY KEY,
            importance_name TEXT
        )
        """
    )

    query.exec("SELECT COUNT(*) FROM importance")
    query.next()
    if query.value(0) == 0:
        query.exec("INSERT INTO importance (importance_name) VALUES ('Важливо')")
        query.exec("INSERT INTO importance (importance_name) VALUES ('Не важливо')")

    query.exec(
        """
        CREATE TABLE IF NOT EXISTS urgency (
            id INTEGER PRIMARY KEY,
            urgency_name TEXT
        )
        """
    )

    query.exec("SELECT COUNT(*) FROM urgency")
    query.next()
    if query.value(0) == 0:
        query.exec("INSERT INTO urgency (urgency_name) VALUES ('Терміново')")
        query.exec("INSERT INTO urgency (urgency_name) VALUES ('Не терміново')")

    query.exec(
        """
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY,
            status_name TEXT
        )
        """
    )

    query.exec("SELECT COUNT(*) FROM status")
    query.next()
    if query.value(0) == 0:
        query.exec("INSERT INTO status (status_name) VALUES ('Виконано')")
        query.exec("INSERT INTO status (status_name) VALUES ('Не виконано')")

    stm = QtSql.QSqlRelationalTableModel(parent=window)
    stm.setTable('actions')
    stm.setSort(1, QtCore.Qt.SortOrder.AscendingOrder)
    stm.setRelation(3, QtSql.QSqlRelation('importance', 'id', 'importance_name'))
    stm.setRelation(4, QtSql.QSqlRelation('urgency', 'id', 'urgency_name'))
    stm.setRelation(5, QtSql.QSqlRelation('status', 'id', 'status_name'))
    stm.select()
    stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Час')
    stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Подія')
    stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, 'Важливість')
    stm.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, 'Терміновість')
    stm.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, 'Статус')

    vbox = QtWidgets.QVBoxLayout()
    tv = QtWidgets.QTableView()
    tv.setModel(stm)

    tv.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(tv))
    tv.setItemDelegateForColumn(4, QtSql.QSqlRelationalDelegate(tv))
    tv.setItemDelegateForColumn(5, QtSql.QSqlRelationalDelegate(tv))

    timeDelegate = TimeDelegate(tv)
    tv.setItemDelegateForColumn(1, timeDelegate)

    tv.hideColumn(0)
    tv.setColumnWidth(1, 60)
    tv.setColumnWidth(2, 225)
    tv.setColumnWidth(3, 100)
    tv.setColumnWidth(4, 100)
    tv.setColumnWidth(5, 100)

    vbox.addWidget(tv)
    btnAdd = QtWidgets.QPushButton("&Додати запис")
    btnAdd.clicked.connect(addRecord)
    vbox.addWidget(btnAdd)
    btnDel = QtWidgets.QPushButton("&Видалити запис")
    btnDel.clicked.connect(delRecord)
    vbox.addWidget(btnDel)
    window.setLayout(vbox)
    window.resize(550, 250)
    window.show()
    sys.exit(app.exec())
