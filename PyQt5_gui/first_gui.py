import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()


        self.setWindowTitle("Testing GUI")
        self.setWindowIcon(QIcon("/home/_dudul/python/pythong-1/PyQt5_gui/images.png"))
        self.setGeometry(0,0,500,500)

        label = QLabel("Hello ", self)
        label.setFont(QFont("Lora", 30))
        label.setGeometry(0,0,500,500)
        label.setStyleSheet("color: blue")
        label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("/home/_dudul/python/pythong-1/PyQt5_gui/images.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

def main():
    if os.path.exists("/home/_dudul/python/pythong-1/PyQt5_gui/icon.jpeg"):
        print("exist")
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("AlarmApp")
    app.setDesktopFileName("AlarmApp")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()