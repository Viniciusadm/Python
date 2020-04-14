from random import randint
numerosLista = list()
pares = list()

def sorteia():
    for c in range(1, 6):
        numerosLista.append(randint(1, 20))
    print(f'Os números sorteados foram ', end='')
    for c, d in enumerate(numerosLista):
        if c + 1 != len(numerosLista):
            print(d, end=', ')
        else:
            print(d)

def somaPar(numeros):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
    soma = sum(pares)
    print('Somando os valores pares de ', end='')
    for c in numeros:
        print(c, end=', ')
    print(f'temos {soma}')

sorteia()
somaPar(numerosLista)