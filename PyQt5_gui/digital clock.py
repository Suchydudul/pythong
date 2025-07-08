import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__ (self):
        super().__init__()
        self.time_label = QLabel("hi",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DIgital Clock")
        self.setGeometry(500,500,500,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
        "font-size: 200px;"
        "color: green;"
        "font-family: FreeSerif;" )
        self.setStyleSheet("background-color: black;")
        self.update_time()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())