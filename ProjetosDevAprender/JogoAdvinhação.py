from random import randint
from funcs import desempacotarLista, apagarTela

class AdvinharNumero:
    def __init__(self):
        self.valorInicial = 1
        self.valorFinal = 100
        self.contador = 0
        self.numeros = []
    

    def gerarNumero(self):
        self.numeroSorteado = randint(self.valorInicial, self.valorFinal)

    def tentarNovamente(self, msg):
        self.contador += 1
        apagarTela()
        self.mostrarTentativas()
        self.resposta = int(input(msg))
        self.numeros.append(self.resposta)

    def obterResposta(self):
        self.resposta = int(input('Escolha um número entre 1 e 100: '))
        self.numeros.append(self.resposta)
        self.contador += 1
        while self.numeroSorteado != self.resposta:
            if self.numeroSorteado > self.resposta:
                self.tentarNovamente('Tente um número maior: ')
            elif self.numeroSorteado < self.resposta:
                self.tentarNovamente('Tente um número menor: ')

    def mostrarTentativas(self):
        print('Números tentados: ', end='')
        desempacotarLista(self.numeros, ' - ')

    def iniciar(self):
        apagarTela()
        print('Um número foi sorteado.')
        self.gerarNumero()
        self.obterResposta()                
        apagarTela()
        self.mostrarTentativas()
        print(f'Você acertou o número {self.numeroSorteado} em {self.contador} tentativas')

jogo = AdvinharNumero()
jogo.iniciar()