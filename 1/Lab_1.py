# import necessary modules
import sys, os.path
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QFont, QPixmap

class TeacherProfile(QWidget):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):

        self.setGeometry(50, 50, 350, 500)
        self.setWindowTitle("Студент")
        self.displayImages()
        self.displayStudentInfo()

        self.show()

    def displayImages(self):
        background_image = "1/images/background.jpg"
        student_image = "1/images/student.jpg"

        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found.")

        try:
            with open(student_image):
                user_image = QLabel(self)
                pixmap = QPixmap(student_image)
                user_image.setPixmap(pixmap)
                user_image.move(75, 23)
        except FileNotFoundError:
            print("Image not found.")

    def displayStudentInfo(self):

        teacher_name = QLabel(self)
        teacher_name.setText("Дмитро Хома")
        teacher_name.move(15, 300)
        teacher_name.setFont(QFont('Arial', 19))

        position_title = QLabel(self)
        position_title.setText("Навчальний заклад \n"
                               "та група: ")
        position_title.move(15, 350)
        position_title.setFont(QFont('Courier New', 17))

        position = QLabel(self)
        position.setText("ХПІ КН-321В")
        position.setWordWrap(True)
        position.move(15, 400)
        position.setFont(QFont('Times New Roman', 14))

        course_title = QLabel(self)
        course_title.setText("Термін навчання")
        course_title.move(15, 430)
        course_title.setFont(QFont('Courier New', 17))

        course = QLabel(self)
        course.setText("2021-2025")
        course.setWordWrap(True)
        course.move(15, 455)
        course.setFont(QFont('Times New Roman', 14))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TeacherProfile()
    sys.exit(app.exec())
