from datetime import datetime

class Historico:
    def __init__(self):
        self.aberturaConta = datetime.today()
        self.transacoes = []

    def imprimir(self):
        print(f'data abertura: {self.aberturaConta}')
        print('trasações: ')
        for c in self.transacoes:
            print('-', c)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    totalContas = 0
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
        Conta.totalContas += 1

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Deposito de R${valor}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de R${valor}')
            print(f'Foram sacados R${valor}')
        else:
            print('Saldo insuficiente')

    def extrato(self):
        print(f'numero: {self.numero} \nnome: {self.titular.nome} {self.titular.sobrenome} \nsaldo: {self.saldo}')
        self.historico.transacoes.append(f'Retirada de extrato R${self.saldo}')

    def transferir(self, valor, destino):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f'R${valor} para a conta {destino}')
        else:
            print('Saldo insuficiente')
