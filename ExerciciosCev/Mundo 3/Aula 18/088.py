from random import randint
from time import sleep
lista = list()
mega = 'Mega Sena'

print('=' * 19)
print(f'{mega:^19}')
print('=' * 19)

while True:
    jogos = int(input('Quantos jogos você quer que eu sorteie? '))
    if jogos <= 50:
        break
    while True:
        jogos = int(input('Escolha no máximo 50 jogos: '))
        if jogos <= 50:
            break
    break

for c in range(1, jogos + 1):
    for d in range(0, 6):
        while True:
            numero = randint(1, 60)
            if numero not in lista:
                lista.append(numero)
            if len(lista) == 6:
                break
        break
    c = str(c)
    if len(c) == 1:
        print(f'Jogo 0{c}: ', end='')
    else:
        print(f'Jogo {c}: ', end='')
    for n, e in enumerate(sorted(lista)):
        if n + 1 < 5:
            print(f'{e:>-2}', end=', ')
        elif n + 1 == 5:
            print(f'{e:>-2}', end=' ')
        else:
            print(f'e {e:>-2}')
    lista.clear()
    sleep(0.5)