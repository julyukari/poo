class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.falando=False
        self.comendo=False
        self.dormindo=False
    def falar(self):
         print(f"{self.nome} começou a falar.")
    def comer(self ,comer):
        if self.comendo==True:
            print("Não pode comer,pois já está comendo")
        self.comer=comer
        print(f"esta comendo {self.comer}.")
    def dormir(self):
        print("e depois vai dormir")


class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.peso = peso
        self.dormindo = False
        self.falando = False
        self.comendo = False

    def dormir(self):
        if self.dormindo == True:
            print(f"O {self.nome} ja está dormindo")
        elif self.comendo == True:
            print(f" O{self.nome} não pode dormir por que esta falando.")
        elif self.dormindo == True:
            print(f"O {self.nome} não pode dormir porque esta comendo")
        else:
            print(f"O bichinho foi dormi... ZZZZ")
            self.dormindo =True


class Conta():
    def __init__(self,nome,numero,saldo,tipo, status):
        self.nome=nome
        self.numero=numero
        self.saldo=0
        self.tipo=tipo
        self.status=False
        self.depositar= self.saldo
    def ativarConta(self):
        if self.status == True:
           print("Sua conta  ja esta ativada !")
        else:
            self.status = True
            print("conta ativada com sucesso")
    def statusConta(self):
        if self.statusConta == True:
           print ("sua conta esta ativa")
        else:
           print("sua conta esta desativada")








