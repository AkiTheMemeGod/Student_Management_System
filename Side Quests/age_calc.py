import sys
from PyQt6.QtWidgets import *
from datetime import datetime


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("DD/MM/YYYY: ")
        self.birth_date_edit = QLineEdit()

        calc_butt = QPushButton("Calculate")
        calc_butt.clicked.connect(self.calc)
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.birth_date_edit, 1, 1)
        grid.addWidget(calc_butt, 3, 0, 1, 2)
        grid.addWidget(self.output_label, 4, 0, 2, 2)

        self.setLayout(grid)

    def calc(self):
        today = datetime.now().year
        birth = self.birth_date_edit.text()
        age = today - int(birth)
        self.output_label.setText(f"{self.name_line_edit.text()}'s Age is : {str(age)}.")


app = QApplication(sys.argv)
age_calc = Calculator()
age_calc.show()
sys.exit(app.exec())
