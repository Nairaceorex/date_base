from PyQt5.QtCore import Qt, QModelIndex, QAbstractTableModel


class FileTableModel(QAbstractTableModel):
    def __init__(self,name, filedb, parent, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.filename = name
        self.db = filedb
        self.f = open(self.filename, "r+")

    def rowCount(self, parent=QModelIndex()):
        return self.db.rowCount()

    def columnCount(self, parent=QModelIndex()):
        return 4

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role != Qt.DisplayRole:
            return None
        return self.db.data(column, row)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            column = index.column()
            self.db.setdata(column, row, value)
            return True

    def __repr__(self):
        return self.db.__repr__()