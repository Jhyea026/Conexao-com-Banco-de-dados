import mysql.connector

class dataBase:
    
    def __init__(self):
        self.bd = None
            
    def conectar(self):
        self.bd = mysql.connector.connect(host="localhost", database="DataBaseAN", 
                                user="root", password="8425867")
        print("Conexão realizada com sucesso!")
        return self.bd