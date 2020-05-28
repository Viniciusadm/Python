from random import randint

class SimuladorDeDado:
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem).upper()
        if resposta == 'S':
            self.gerarValorDado()
        elif resposta == 'N':
            print('Agradecemos a utilização')
        else:
            print('Favor digitar S ou N')
            simulador.Iniciar()            

    def gerarValorDado(self):
        print(randint(self.valorMinimo, self.valorMaximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
