import sqlite3 
from sqlite3 import Error

class Conexao:

    def __init__(self):
        self.dataBase = None
        self.conection = None
        self.cursor = None
        self.connected = None

    def conecte(self):
        try:
            self.conection = sqlite3.connect()
            self.cursor = self.conection.cursor()
            self.connected = True
        except Error as error:
            return error

    def execute(self, comando):
        if self.connected:
            try:
                self.cursor.execute(comando)
                return True
            except Error as error:
                return error
        else:
            return False