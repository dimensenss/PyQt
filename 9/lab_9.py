from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
dark_palette = QtGui.QPalette()

# назва групи та роки видання синглів
window = QtWidgets.QWidget()
window.setWindowTitle("Rammstein singles")
window.resize(800, 800)

# зображення групи в іконці вікна
ico = QtGui.QIcon('ico.png')
app.setWindowIcon(ico)

# створення графічної сцени
scene = QtWidgets.QGraphicsScene(0.0, 0.0, 750.0, 750.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.darkRed)

# додавання зображень обкладинок синглів
single_1 = scene.addPixmap(QtGui.QPixmap("single_1.jpg"))
single_1.setPos(QtCore.QPointF(0.0, 0.0))
single_1.setScale(0.8)
single_1.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_1.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_2 = scene.addPixmap(QtGui.QPixmap("single_2.jpg"))
single_2.setPos(QtCore.QPointF(255.0, 0.0))
single_2.setScale(0.8)
single_2.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_2.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_3 = scene.addPixmap(QtGui.QPixmap("single_3.jpg"))
single_3.setPos(QtCore.QPointF(510.0, 0.0))
single_3.setScale(0.8)
single_3.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_3.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_4 = scene.addPixmap(QtGui.QPixmap("single_4.jpg"))
single_4.setPos(QtCore.QPointF(0.0, 255.0))
single_4.setScale(0.8)
single_4.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_4.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_5 = scene.addPixmap(QtGui.QPixmap("single_5.jpg"))
single_5.setPos(QtCore.QPointF(255.0, 255.0))
single_5.setScale(0.8)
single_5.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_5.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_6 = scene.addPixmap(QtGui.QPixmap("single_6.jpg"))
single_6.setPos(QtCore.QPointF(510.0, 255.0))
single_6.setScale(0.8)
single_6.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_6.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_7 = scene.addPixmap(QtGui.QPixmap("single_7.jpg"))
single_7.setPos(QtCore.QPointF(0.0, 510.0))
single_7.setScale(0.8)
single_7.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_7.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_8 = scene.addPixmap(QtGui.QPixmap("single_8.jpg"))
single_8.setPos(QtCore.QPointF(255.0, 510.0))
single_8.setScale(0.8)
single_8.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_8.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

single_9 = scene.addPixmap(QtGui.QPixmap("single_9.jpg"))
single_9.setPos(QtCore.QPointF(510.0, 510.0))
single_9.setScale(0.8)
single_9.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
single_9.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
