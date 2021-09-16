from random import randint

def computer_move(palitos, jogadas):
    for c in range(jogadas, 0, -1):
        tirados = palitos - c
        if (tirados % (jogadas + 1) == 0):
            break
    else:
        return [palitos - jogadas, jogadas]
    return [tirados, c]

def player_move(palitos, jogadas):
    while True:
        jogada = int(input('Quantidade a ser tirado: '))
        if (jogada <= jogadas and jogada > 0):
            break
        else:
            print('Quantidade inválida')
    return [palitos - jogada, jogada]

def game():
    palitos = randint(7, 22)
    jogadas = randint(2, 5)

    print(f'Palitos: {palitos}\nJogadas: {jogadas}')
    if (palitos % (jogadas + 1) == 0):
        print('Você começa!')
        while True:
            resultado = player_move(palitos, jogadas) 
            palitos = resultado[0]
            tirados = resultado[1]
            print(f'Você tirou {tirados} palitos restando {palitos}')
            print(40 * '-')
            if (palitos <= 0):
                print('Você venceu')
                break
            resultado = computer_move(palitos, jogadas) 
            palitos = resultado[0]
            tirados = resultado[1]
            print(f'O computador tirou {tirados} palitos restando {palitos}')
            print(40 * '-')
            if (palitos <= 0):
                print('O computador venceu')
                break
    elif (palitos % (jogadas + 1) != 0):
        print('Computador começa!')
        while True:
            resultado = computer_move(palitos, jogadas) 
            palitos = resultado[0]
            tirados = resultado[1]
            print(f'O computador tirou {tirados} palitos restando {palitos}')
            print(40 * '-')
            if (palitos <= 0):
                print('O computador venceu')
                break
            resultado = player_move(palitos, jogadas) 
            palitos = resultado[0]
            tirados = resultado[1]
            print(f'Você tirou {tirados} palitos restando {palitos}')
            print(40 * '-')
            if (palitos <= 0):
                print('Você venceu')
                break

game()
