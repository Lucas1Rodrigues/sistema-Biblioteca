class Transacao:
    def __init__(self,valor:float, nome:str, data:str,tipo:str):
        if isinstance(valor,float) or isinstance(valor,int):
            if valor > 0:
                self.valor = valor
        else:
            raise ValueError("Apenas valores maiores que 0 ")
        self.nome = nome
        self.data = data
        if tipo in ["receita","despesa"]:
            self.tipo = tipo.lower()
        else:
            raise ValueError("Apenas valores 'receita' ou 'despesa'")

class Conta:
    def __init__(self, nome='', id = 0):
        self.nome = nome
        self.id = id
        self.transacoes = []    

    def adicionar_transacao(self,transacao):
        if not isinstance(transacao,Transacao):
            raise ValueError("transacao possui um erro")
        elif 
            self.transacoes.append(transacao)

    def calcular_conta(self):
