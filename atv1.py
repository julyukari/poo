from biblioteca import Pessoa
aluno01=Pessoa("July",29,80)
aluno02=Pessoa("Victor",20,76)
print(f"{aluno01.nome} , tem {aluno01.idade} anos e pesa {aluno01.peso}")
print(f"{aluno02.nome} , tem {aluno02.idade} anos e pesa {aluno02.peso}")
aluno01.nome="July Yukari de Santana Montes"
print(f"{aluno01.nome} , tem {aluno01.idade} anos e pesa {aluno01.peso}")
aluno01.falar()
aluno01.comer("pipoca")
aluno01.dormir()


