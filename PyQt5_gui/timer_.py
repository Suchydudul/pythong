import sys 
import time
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer, QTime, Qt

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.textbox = QLabel("Please set a time", self)
        self.input_edit = QLineEdit(self)
        self.button =QPushButton("Submit", self)
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
        text = self.input_edit.text()

        for second in range(int(text)):
            self.textbox.setText(str(second))
            app.processEvents
            time.sleep(1)
            print(second+1, flush=True)






def main():
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()