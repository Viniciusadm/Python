from random import shuffle

animesVotar = []
animesPerdidos = [[]]
ranking = []

def printarOpcoes(opcao, indice):
    if animesVotar[indice][-1:-2:-1] == '\n':
        print(f'{opcao}- {animesVotar[indice]}', end='')
    else:
        print(f'{opcao}- {animesVotar[indice]}')

with open('animes.txt', 'r') as file:
    for c in file:
        animesVotar.append(c)
        shuffle(animesVotar)
        tamanho = len(animesVotar)

while len(animesVotar) != 1:
    print('Escolha um anime: ')
    printarOpcoes(1, 0)
    printarOpcoes(2, 1)
    opcao = int(input('Opção: '))
    animesVotar.append(animesVotar[opcao - 1])
    animesVotar.remove(animesVotar[opcao - 1])
    if len(animesPerdidos[0]) == tamanho / 2:
        animesPerdidos.insert(0, [])
        tamanho = len(animesVotar)
    animesPerdidos[0].append(animesVotar[0])
    animesVotar.remove(animesVotar[0])
else:
    ranking.append(animesVotar[0])

    for c in animesPerdidos:
        if len(c) == 1:
            ranking.append(c[0])
            animesPerdidos.pop(0)
            animesVotar = []
        else:
            while len(c) != 1:
                print('Escolha um anime: ')
                printarOpcoes(1, 0)
                printarOpcoes(2, 1)
                opcao = int(input('Opção: '))
                c.append(c[opcao - 1])
                c.remove(c[opcao - 1])
                if len(animesPerdidos[0]) == tamanho / 2:
                    animesPerdidos.insert(0, [])
                    tamanho = len(c)
                animesPerdidos[0].append(c[0])
                c.remove(c[0])
