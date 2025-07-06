import sys
import os
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def update_time(self):
        current_time = time.asctime()[11:19]
        self.label.setText(f"Current time: {current_time}")
    
    def __init__ (self):
        super().__init__()

        current_date = time.asctime()
        self.setWindowTitle("Testing GUI")
        self.setWindowIcon(QIcon("/home/_dudul/python/pythong-1/PyQt5_gui/images.png"))
        self.setGeometry(0,0,500,500)


        self.label = QLabel(f"Current time: {current_date[11:19]}", self)
        self.label.setFont(QFont("Lora", 30))
        self.label.setGeometry(0,0,500,500)
        self.label.setStyleSheet("color: blue")
        self.label.setAlignment(Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)





     

        #pixmap = QPixmap("/home/_dudul/python/pythong-1/PyQt5_gui/images.png")
        #label.setPixmap(pixmap)
        #label.setScaledContents(True)

def main():
    current_date = time.asctime()
    print(current_date[11:19])
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("AlarmApp")
    app.setDesktopFileName("AlarmApp")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()