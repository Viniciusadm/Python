contador = 0

numeroUm = int(input('Digite o primeiro número: '))
numeroDois = int(input('Digite o segundo número: '))
numeroTres = int(input('Digite o terceiro número: '))
numeroQuatro = int(input('Digite o quarto número: '))

tupla = (numeroUm, numeroDois, numeroTres, numeroQuatro)

print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu pela primeira vez na posição {tupla.index(3) + 1}')
else:
    print('O 3 não apareceu')

for c in tupla:
    if c % 2 == 0:
        contador += 1

if contador != 0:
    print(f'Os números pares foram: ', end='')
    for c in tupla:
        if c % 2 == 0:
            print(c, end=' ')