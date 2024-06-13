import sys
from PyQt6.QtWidgets import *


class Speed(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        dist_lab = QLabel("Distance")
        self.distance = QLineEdit()

        time_lab = QLabel("Time (hours)")
        self.time = QLineEdit()

        calc_butt = QPushButton("Calculate Speed")
        calc_butt.clicked.connect(self.calc)

        self.answer = QLabel("")

        self.system = QComboBox()
        self.system.addItems(["Metric(km)", "Imperial(miles)"])

        grid.addWidget(dist_lab, 0, 0)
        grid.addWidget(self.distance, 0, 1)

        grid.addWidget(time_lab, 1, 0)
        grid.addWidget(self.time, 1, 1)

        grid.addWidget(calc_butt, 2, 0, 1, 2)

        grid.addWidget(self.answer, 3, 0, 1, 2)

        grid.addWidget(self.system, 0, 2)

        self.setLayout(grid)

    def calc(self):
        if self.system.currentText() == "Metric(km)":
            speed = int(self.distance.text()) / int(self.time.text())
            self.answer.setText(f"Average speed was {speed} km/h")
        if self.system.currentText() == "Imperial(miles)":
            speed = (int(self.distance.text()) * 0.62) / int(self.time.text())
            self.answer.setText(f"Average speed was {speed} mi/h")


app = QApplication(sys.argv)
speed_calc = Speed()
speed_calc.show()
sys.exit(app.exec())
