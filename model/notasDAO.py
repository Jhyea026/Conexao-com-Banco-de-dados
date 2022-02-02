from Config.dataBase import dataBase
from model.notas import notas


class notasDAO:
    def __init__(self):
        pass
    
    def cadastrar(self, notas):
        bd = dataBase().conectar()
        
        cursor = bd.cursor()
        
        script = f"insert into nota(n1, n2, n3, media) values ('{notas.getN1()}', '{notas.getN2()}', '{notas.getN3()}', '{notas.Final()}')"
        cursor.execute(script)
        bd.commit()
        print("Notas cadastradas com sucesso!")
        
    def media(self, media):
        bd = dataBase().conectar()
        cursor = bd.cursor()
        script = "insert into nota(media) values('"+media+"')"
        cursor.execute(script)
        bd.commit()
        print("media calculada*")
        
    def deletar(self, media):
        bd = dataBase().conectar()
        cursor = bd.cursor()
        script = "delete from nota where media = '"+media+"'"
        cursor.execute(script)
        bd.commit()
        print("Notas deletadas com sucesso!")
        
    def listar():
        bd = dataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from nota")
        result = cursor.fetchall()
        
        print("resultados:")
        return result