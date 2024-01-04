from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)

# Create a QPdfWriter instance and set the output PDF file name
writer = QtGui.QPdfWriter("output.pdf")

# Create a custom page size (200 x 120 mm)
custom_page_size = QtCore.QSizeF(180.0, 90.0)

# Set up the page layout for the PDF using the custom page size
layout = QtGui.QPageLayout()
layout.setPageSize(QtGui.QPageSize(custom_page_size, QtGui.QPageSize.Unit.Millimeter))
layout.setOrientation(QtGui.QPageLayout.Orientation.Portrait)
writer.setPageLayout(layout)

# Create a QPainter instance and begin painting on the PDF
painter = QtGui.QPainter()
painter.begin(writer)

# Get the dimensions of the PDF page in pixels
page_size = layout.paintRectPixels(writer.resolution())
page_width = int(page_size.width())
page_height = int(page_size.height())

for i in range(1, 4):
    file_name = str(i) + '.jpg'

    # Load the image and scale it to fit the page while maintaining aspect ratio
    pixmap = QtGui.QPixmap(file_name)
    pixmap = pixmap.scaled(page_width, page_height, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)

    # Draw the scaled pixmap onto the PDF page
    painter.drawPixmap(0, 0, pixmap)

    # Create a new page in the PDF
    if i < 3:
        writer.newPage()

# Finish painting and close the PDF
painter.end()
