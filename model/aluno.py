class aluno:
    def __init__(self, id, nome, periodo):
        self.id = id
        self.nome = nome
        self.periodo = periodo
        
    def getId(self):
        return self.id
        
    def getNome(self):
        return self.nome
    
    def getPeriodo(self):
        return self.periodo