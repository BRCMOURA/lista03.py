# 1) Crie uma classe chamada "Carro" com os atributos marca, ano e cor. Em seguida, crie um objeto dessa classe e imprima seus atributos.

# class Carro:
#     def __init__(self, marca, ano, cor):
#         self.marca = marca
#         self.ano = ano
#         self.cor = cor
    
#     def informacaoSaida(self):
#         print(f'O carro de marca', self.marca, 'ano', self.ano, 'e cor', self.cor)

# carro1 = Carro(input('Marca: '), input('Ano: '), input('Cor: '))
# carro2 = Carro(input('Marca: '), input('Ano: '), input('Cor: '))

# carro1.informacaoSaida()
# carro2.informacaoSaida()

# 2) Crie uma classe "Pessoa" e o usuário insira os atributos de dados pessoais fictícios. Crie um objeto e exiba uma mensagem usando esses atributos.

# class Pessoa:
#     def __init__(self, nome, sobrenome, idade, cpf, cidade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade
#         self.cpf = cpf
#         self.cidade = cidade

#     def informacaoSaida(self):
#         print(f'O nome do usuário é:', self.nome, self.sobrenome,',sua idade é', self.idade,'anos, CPF:', self.cpf, ',cidade:', self.cidade)

# pessoa1 = Pessoa(input('Nome: '), input('Sobrenome: '), input('Idade: '), input('CPF: '), input('Cidade: '))
# pessoa2 = Pessoa(input('Nome: '), input('Sobrenome: '), input('Idade: '), input('CPF: '), input('Cidade: '))

# pessoa1.informacaoSaida()
# pessoa2.informacaoSaida()

# 3) Crie uma classe "ContaBancaria", contendo dados da conta, incluindo o atributo "saldo" e igual a R$ 1000,00. Adicione métodos para depositar valor a essa conta
# e em seguida imprima o saldo atual e nome do cliente.

# class ContaBancaria:
#     def __init__(self, nome_cliente):
#         self.nome = nome_cliente
#         self.saldo = 1000
    
#     def depositar(self, valor):
#          self.saldo += valor
#          print(f"Depósito realizado com sucesso! Saldo atual: R$ {self.saldo}")

# conta = ContaBancaria("Seu Nome")
# conta.depositar(500)
     