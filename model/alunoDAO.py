from Config.dataBase import dataBase
from model.aluno import aluno


class alunoDAO:
    def __init__(self):
        pass
    
    def cadastrar(self, aluno):
        bd = dataBase().conectar()
        
        cursor = bd.cursor()
        
        script = "insert into aluno(nome, periodo) values ('"+aluno.getNome()+"', '"+aluno.getPeriodo()+"')"
        cursor.execute(script)
        bd.commit()
        print("Aluno cadastrado com sucesso!")
        
    def deletar(self, id):
        bd = dataBase().conectar()
        cursor = bd.cursor() 
        script = "delete from aluno where id = '"+id+"'"
        cursor.execute(script)
        bd.commit()
        print("Aluno removido com sucesso!")
        
    def buscar(self, id):
        bd = dataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from aluno where id = '"+id+"'")
        result = cursor.fetchone()
        print("resultados da busca:")
        return(result)
        
    def listar():
        bd = dataBase().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from aluno")
        result = cursor.fetchall()
        
        print("\nresultados:\n")
        return result
    