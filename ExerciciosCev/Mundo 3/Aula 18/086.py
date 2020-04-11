lista = [[], [], []]

for matrizl in range(0, 3):
    for matrizc in range(0, 3):
        numero = int(input(f'Digite um valor para [{matrizl}], [{matrizc}]: '))
        lista[matrizl].append(numero)

for matrizl in lista:
    for matrizc in matrizl:
        print('[', end='')
        print((f'{matrizc:^5}'), end='')
        print(']', end='')
    print('\n', end='')