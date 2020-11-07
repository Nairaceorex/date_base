import os


class FileDB:
    def __init__(self, name):
        self.filename = name
        self.f = open(self.filename, 'r+')

    def data(self, column, row):
        self.f.seek(100 * column + 400 * row, 0)
        return self.f.read(100)

    def rowCount(self):
        return os.path.getsize(self.filename)/400

    def columnCount(self):
        return 4

    def setdata(self, column, row, value):
        self.f.seek(100 * column + 400 * row, 0)
        self.f.write(str(value)[0:99] + '\0' * (100 - len(str(value))))

    def __repr__(self):
        max_size = 0
        for i in range(int(os.path.getsize(self.filename) / 100)):
            self.f.seek(i * 100, 0)
            temp = self.f.read(100)
            j = 0
            temp_size = 0
            while temp[j] != "\0":
                temp_size += 1
                j += 1
            if temp_size > max_size:
                max_size = temp_size
        string = "++"
        for i in range(4):
            for j in range(max_size):
                string += "-"

            string += "++"
        string += "\n"
        for i in range(int(self.rowCount())):
            string += "|"
            for j in range(int(self.columnCount())):
                string += "|"
                self.f.seek(i * 400 + j * 100, 0)
                temp = self.f.read(max_size)
                k = 0
                while k < max_size:
                    if temp[k] == "\0":
                        string += " "
                    string += temp[k]
                    k += 1
                string += "|"
            string += "|"
            string += "\n"
            string += "++"
            for j in range(4):
                for k in range(max_size):
                    string += "-"
                string += "++"
            string += "\n"
        return string