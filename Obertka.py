import sqlite3


class Obertka:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = sqlite3.connect("test.db")

    def crateTable(self, name: str, vocab):
        c = self.conn.cursor()
        s = []
        for i in vocab:
            s.append(f"{i} {vocab[i]}")
        value = ", ".join(s)
        c.execute(f"CREATE TABLE if not exists {name} (ID INT PRIMARY KEY, {value})")
        self.conn.commit()

    def InsertValues(self, name, vocab):
        c = self.conn.cursor()
        try:
            id = c.execute(f"Select * FROM {name}").fetchall()[-1][0] + 1
        except:
            id = 1
        s = []
        for i in vocab:
            s.append("?")
        value = ", ".join(s)
        c.execute(f"INSERT INTO {name} VALUES ({id} , {value})", vocab)
        self.conn.commit()

    def getTable(self, name):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM {name} ')
        test = c.fetchall()
        output = []
        for i in test:
            temp=[]
            for j in i:
                temp.append(j)
            output.append(temp)
        return output

    def set(self, name, id, column, value):
        c = self.conn.cursor()
        c.execute(f'UPDATE {name} SET {column} = "{value}" WHERE ID = {id}')
        self.conn.commit()

    def getHeader(self, name):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {name}")
        headers = []
        for head in c.description:
            headers.append(head[0].upper())
        return headers