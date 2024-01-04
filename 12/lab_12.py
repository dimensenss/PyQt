import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer
import os

class SlideshowApp(QMainWindow):
    def __init__(self, image_folder, interval=2000, scale_factor=0.5):
        super().__init__()

        self.image_folder = image_folder
        self.image_list = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

        self.current_index = 0

        self.interval = interval
        self.scale_factor = scale_factor
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_next_image)
        self.timer.start(self.interval)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.label = QLabel()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(central_widget)

        self.show_image()
        self.setWindowTitle("Rammstein singles and albums")
        self.resize(400, 400)

    def show_image(self):
        if self.image_list:
            image_path = os.path.join(self.image_folder, self.image_list[self.current_index])
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(
                int(pixmap.width() * self.scale_factor),
                int(pixmap.height() * self.scale_factor),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.label.setPixmap(scaled_pixmap)

    def show_next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_list)
        self.show_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ico = QIcon('ico.png')
    app.setWindowIcon(ico)
    image_folder = './images'
    scale_factor = 1.0
    slideshow = SlideshowApp(image_folder, scale_factor=scale_factor)
    slideshow.show()
    sys.exit(app.exec())
