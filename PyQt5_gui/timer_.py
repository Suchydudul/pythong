import sys 
import time
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer, QTime, Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.textbox = QLabel("Please set a time", self)
        self.input_edit = QLineEdit(self)
        self.button =QPushButton("Submit", self)
        self.timer = QTimer()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.input_edit)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

        self.textbox.setAlignment(Qt.AlignCenter)
        self.textbox.setStyleSheet(
        "font-size: 50px;"
        "color: green;"
        "font-family: FreeSerif;" )


        self.input_edit.setStyleSheet(
        "background: white;" \
        "color: black;")

        self.input_edit.setPlaceholderText("Enter Time")
        self.button.clicked.connect(self.submit)

    def submit(self):
        self.seconds = int(self.input_edit.text())
        self.timer.start(1000)
        self.timer.timeout.connect(self.showtime)
        self.button.setEnabled(False)
        
    def showtime(self):
        if self.seconds == 0:
            self.timer.stop()
            self.button.setEnabled(True)
        self.textbox.setText(str(self.seconds))
        self.seconds -= 1
        

def main():
    app = QApplication(sys.argv)
    timer = MainWindow()
    timer.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()