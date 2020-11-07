from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

from Obertka import Obertka


class CustomTableModel(QAbstractTableModel):
    def __init__(self, TableName: str, parent, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.db = Obertka()
        self.table_name = TableName
        self.head_name = self.db.getHeader(self.table_name)

    def rowCount(self, parent=QModelIndex()):
        return len(self.db.getTable(self.table_name))

    def columnCount(self, parent=QModelIndex()):
        return len(self.db.getTable(self.table_name)[0])

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role == Qt.DisplayRole and Qt_Orientation == Qt.Horizontal:
            if p_int < len(self.head_name):
                return self.head_name[p_int]
        return QVariant()

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role != Qt.DisplayRole:
            return None
        return self.db.getTable(self.table_name)[row][column]

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row=index.row()
            column=index.column()
            self.db.set(self.table_name, row+1, self.head_name[column], value)
            return True