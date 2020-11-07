import sys

from PyQt5.QtWidgets import QWidget, QTableView, QCheckBox, QPushButton, QApplication, QMainWindow

from CustomTableModel import CustomTableModel
from FileDB import FileDB
from FileTableModel import FileTableModel


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.checkbox.stateChanged.connect(self.change)
        self.button.clicked.connect(self.printfile)

    def initUi(self):
        self.resize(self.parent().size())
        self.tableview = CustomTableModel("Staff", self)
        self.filedb = FileDB("test.txt")
        self.tablefile = FileTableModel("test.db",self.filedb, self)
        self.showtable = QTableView(self)
        self.showtable.setModel(self.tableview)
        self.showtable.setGeometry(10, 30, 320, 200)
        self.checkbox = QCheckBox(self)
        self.checkbox.move(350, 50)
        self.check = True
        self.button = QPushButton(self)
        self.button.move(350, 80)

    def change(self):
        if self.check:
            self.showtable.setModel(self.tablefile)
        else:
            self.showtable.setModel(self.tableview)
        self.check = not self.check

    def printfile(self):
        print(self.tablefile)

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    main = QMainWindow()
    w= MyWindow(main)
    main.show()
    qapp.exec()