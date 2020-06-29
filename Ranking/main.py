from random import shuffle

animesVotar = []
animesPerdidos = [[]]
gatilho = 0

while True:
    if gatilho == 0:
        with open('animes.txt', 'r') as file:
            for c in file:
                animesVotar.append(c)
                shuffle(animesVotar)
                tamanho = len(animesVotar)
    else:
        animesVotar = animesVotar[1:]

    while len(animesVotar) != 1:
        print('Escolha um anime: ')
        print(f'1- {animesVotar[0]}', end='')
        print(f'2- {animesVotar[1]}', end='')
        opcao = int(input('Opção: '))
        animesVotar.append(animesVotar[opcao - 1])
        animesVotar.remove(animesVotar[opcao - 1])
        if len(animesPerdidos[0]) == tamanho / 2:
            animesPerdidos.insert(0, [])
            tamanho = len(animesVotar)
        animesPerdidos[0].append(animesVotar[0])
        animesVotar.remove(animesVotar[0])
    else:
        print(f'O vencedor é {animesVotar[0]}')
        print(animesPerdidos)
        gatilho = 1