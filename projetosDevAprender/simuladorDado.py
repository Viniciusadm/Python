from random import randint
from os import system

system('clear')

class RoladorDado:
    def __init__(self):
        self.valorInicial = 1
        self.valorFinal = 6
        self.resposta = 'Você gostaria de gerar um valor? '
    
    def rolarDado(self):
        return randint(self.valorInicial, self.valorFinal)

    def iniciar(self):
        resposta = str(input(self.resposta)).upper()
        if resposta == 'S':
            print(self.rolarDado())
        elif resposta == 'N':
            print('Agradecemos a utilização')
        else:
            system('clear')
            print('Favor digitar S ou N')
            self.iniciar()

simulador = RoladorDado()
simulador.iniciar()
