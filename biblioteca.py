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




