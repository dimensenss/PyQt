from PyQt6 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)

# назва групи у заголовку вікна
window = QtWidgets.QWidget()
window.setWindowTitle("System Of A Down")
window.resize(300, 300)

# зображення групи в іконці вікна
ico = QtGui.QIcon('icon.jpg')
app.setWindowIcon(ico)

# назва групи
name_label = QtWidgets.QLabel('System Of A Down')
name_label.setFont(QtGui.QFont('Times New Roman', 20))
name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
name_label.setStyleSheet('font-weight: bold;\
                         background-color: red;\
                         color: black')

# зображення групи
image_label = QtWidgets.QLabel()
image = QtGui.QPixmap('soad.jpg')
image_label.setPixmap(image)

# стисла інформація про групу
info_label = QtWidgets.QLabel('Background information')
info_label.setFont(QtGui.QFont('Times New Roman', 20))
info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
info_label.setStyleSheet('font-weight: bold;\
                         background-color: red;\
                         color: black')

# походження, музичні жанри, роки існування,
# належність до фірм звукозапису, склад
origin_label = QtWidgets.QLabel('California, USA')
origin_label.setFont(QtGui.QFont('Times New Roman', 16))
genres_label = QtWidgets.QLabel('Alternative metal, nu metal, heavy metal, hard rock, progressive metal')
genres_label.setFont(QtGui.QFont('Times New Roman', 16))
years_label = QtWidgets.QLabel('1994-2006, 2010-forever')
years_label.setFont(QtGui.QFont('Times New Roman', 16))
labels_label = QtWidgets.QLabel('Sony Music, American Recordings, Columbia')
labels_label.setFont(QtGui.QFont('Times New Roman', 16))
members_label = QtWidgets.QLabel('Serj Tankian, Daron Malakian, Shavo Odadjian, John Dolmayan')
members_label.setFont(QtGui.QFont('Times New Roman', 16))

origin_name = QtWidgets.QLabel('Origin:')
origin_name.setFont(QtGui.QFont('Times New Roman', 18))
origin_name.setStyleSheet('font-weight: bold')

genres_name = QtWidgets.QLabel('Genres:')
genres_name.setFont(QtGui.QFont('Times New Roman', 18))
genres_name.setStyleSheet('font-weight: bold')

years_name = QtWidgets.QLabel('Years:')
years_name.setFont(QtGui.QFont('Times New Roman', 18))
years_name.setStyleSheet('font-weight: bold')

labels_name = QtWidgets.QLabel('Labels:')
labels_name.setFont(QtGui.QFont('Times New Roman', 18))
labels_name.setStyleSheet('font-weight: bold')

members_name = QtWidgets.QLabel('Members:')
members_name.setFont(QtGui.QFont('Times New Roman', 18))
members_name.setStyleSheet('font-weight: bold')

form = QtWidgets.QFormLayout()
form.addRow(origin_name, origin_label)
form.addRow(genres_name, genres_label)
form.addRow(years_name, years_label)
form.addRow(labels_name, labels_label)
form.addRow(members_name, members_label)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(name_label)
vbox.addWidget(image_label)
vbox.addWidget(info_label)
vbox.addLayout(form)

window.setLayout(vbox)

window.show()
sys.exit(app.exec())
