from random import randint
from os import system
from funcs import desempacotarLista

class AdvinharNumero:
    def __init__(self):
        self.valorInicial = 1
        self.valorFinal = 100
        self.mensagemInicial = 'Um número foi sorteado.'
        self.mensagemChute = 'Escolha um número entre 1 e 100: '
        self.mensagemMaior = 'Tente um número maior: '
        self.mensagemMenor = 'Tente um número menor: '
        self.contador = 0
        self.numeros = []
    
    def gerarNumero(self):
        self.numeroSorteado = randint(self.valorInicial, self.valorFinal)

    def iniciar(self):
        system('clear')
        self.gerarNumero()
        print(self.mensagemInicial)
        self.resposta = int(input(self.mensagemChute))
        self.numeros.append(self.resposta)
        self.contador += 1

        while self.numeroSorteado != self.resposta:
            if self.numeroSorteado > self.resposta:
                self.contador += 1
                system('clear')
                print('Números tentados: ', end='')
                desempacotarLista(self.numeros, ' - ')
                self.resposta = int(input(self.mensagemMaior))
                self.numeros.append(self.resposta)
            elif self.numeroSorteado < self.resposta:
                self.contador += 1
                system('clear')
                print('Números tentados: ', end='')
                desempacotarLista(self.numeros, ' - ')
                self.resposta = int(input(self.mensagemMenor))
                self.numeros.append(self.resposta)
                
        system('clear')
        print('Números tentados: ', end='')
        desempacotarLista(self.numeros, ' - ')
        print(f'Você acertou o número {self.numeroSorteado} em {self.contador} tentativas')

jogo = AdvinharNumero()
jogo.iniciar()