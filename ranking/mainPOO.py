from random import shuffle

class Ranking:
    def __init__(self):
        self.animesVotar = []
        self.animesPerdidos = [[]]

    def abrirArquivo(self):
        with open('animes.txt', 'r') as self.file:
            for c in self.file:
                self.animesVotar.append(c)
                shuffle(self.animesVotar)
                self.tamanho = len(self.animesVotar)

    def printarOpcoes(self, opcao, indice):
        if self.animesVotar[indice][-1:-2:-1] == '\n':
            print(f'{opcao}- {self.animesVotar[indice]}', end='')
        else:
            print(f'{opcao}- {self.animesVotar[indice]}')

    def escolherOpcao(self):
        while len(self.animesVotar) != 1:
            print('Escolha um anime: ')
            self.printarOpcoes(1, 0)
            self.printarOpcoes(2, 1)
            self.opcao = int(input('Opção: '))
            self.animesVotar.append(self.animesVotar[self.opcao - 1])
            self.animesVotar.remove(self.animesVotar[self.opcao - 1])
            if len(self.animesPerdidos[0]) == self.tamanho / 2:
                self.animesPerdidos.insert(0, [])
                self.tamanho = len(self.animesVotar)
            self.animesPerdidos[0].append(self.animesVotar[0])
            self.animesVotar.remove(self.animesVotar[0])
        else:
            print(f'O vencedor é {self.animesVotar[0]}')
            print(self.animesPerdidos)
        
    def main(self):
        self.abrirArquivo()
        self.escolherOpcao()

iniciar = Ranking()
iniciar.main()