from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
import sys
import sqlite3 as sq

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_act = QAction("Add Student", self)
        file_menu_item.addAction(add_student_act)

        about = QAction("About", self)
        help_menu_item.addAction(about)

        '''Table'''

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.table)
        self.load_data()

    def load_data(self):
        connection = sq.connect("database.db")
        result = connection.execute("select * from students")
        self.table.setRowCount(0)
        for rown, rowd in enumerate(result):
            self.table.insertRow(rown)
            for coln, data in enumerate(rowd):
                self.table.setItem(rown,coln, QTableWidgetItem(str(data)))
        connection.close()
        #comment
        self.table


app = QApplication(sys.argv)
speed_calc = MainWindow()
speed_calc.show()

sys.exit(app.exec())