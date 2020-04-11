lista = [[], [], []]
somaPar = 0
somaColuna = 0

for matrizl in range(0, 3):
    for matrizc in range(0, 3):
        numero = int(input(f'Digite um valor para [{matrizl}], [{matrizc}]: '))
        lista[matrizl].append(numero)

for matrizl in lista:
    for matrizc in matrizl:
        print('[', end='')
        print((f'{matrizc:^5}'), end='')
        print(']', end='')
        if matrizc % 2 == 0:
            somaPar += matrizc
    print('\n', end='')

for linha in range(0, 3):
    somaColuna += lista[linha][2]

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {max(lista[1])}')