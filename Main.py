from model.aluno import aluno
from model.alunoDAO import alunoDAO
from model.notas import notas
from model.notasDAO import notasDAO
from Config.dataBase import dataBase
import statistics

def cadastrarA():
    dao = alunoDAO()
    Nome = input("digite o nome do aluno a ser cadastrado: ")
    Periodo = input("digite o periododo do aluno: ")
    Aluno = aluno(id=None, nome = Nome, periodo=Periodo)
    result = dao.cadastrar(Aluno)
    print(result)

def cadastrarN():
    dao = notasDAO()
    Nota1 = float(input("insira a primeira nota do aluno: "))
    Nota2 = float(input("insira a segunda nota do aluno: "))
    Nota3 = float(input("insira a terceira nota do aluno: "))
    Final = [Nota1,Nota2,Nota3]
    Final = statistics.mean(Final)
    a = notas(Nota1, Nota2, Nota3, round(Final,2))
    dao.cadastrar(a)

def listarA():
    result = alunoDAO.listar()
    print(result)
    
def listarN():
    result = notasDAO.listar()
    print(result)

def buscarA():
    id = input("insira o id do aluno a ser buscado: ")
    dao = alunoDAO()
    result = dao.buscar(id)
    print(result)

def deletarA():
    id = input("insira o id do aluno a ser deletado: ")
    dao = alunoDAO()
    result = dao.deletar(id)
    print(result)
    
def deletarN():
    media = input("insira uma das notas do aluno a ser deletada: ")
    dao = notasDAO()
    result = dao.deletar(str(media))
    print(result)
    
def desconectarBD():
    bd = dataBase().desconectar()
    
def menuA():
    while(True):
        print("\n\n> 1- Cadastrar Aluno \n> 2 - Listar Aluno \n> 3 - Buscar Aluno \n> 4 - Remover Aluno \n> 0 - Voltar")
        opc = input("\n> ")
        if (opc == '1'):
            cadastrarA()
        elif (opc == '2'):
            listarA()
        elif (opc == '3'):
            buscarA()
        elif (opc == '4'):
            deletarA()
        elif (opc == '0'):
            break
    
def menuN():
    while(True):
        print("\n\n> 1- Cadastrar Nota \n> 2 - Listar Nota \n> 3 - Deletar Nota \n> 0 - Voltar")
        opc = input("\n> ")
        if (opc == '1'):
            cadastrarN()
        elif (opc == '2'):
            listarN()
        elif (opc == '3'):
            deletarN()
        elif (opc == '0'):
            break
        
def menu():
    while(True):
        print("\n\n> 1- Alunos \n> 2 - Notas \n> 0 - Sair")
        opc = input("\n> ")
        if (opc == '1'):
            menuA()
        elif (opc == '2'):
            menuN()
        elif (opc == '0'):
            break
          
menu()