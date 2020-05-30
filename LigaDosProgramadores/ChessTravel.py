'''lista = ['A', 1, 'B', 2, 'C', 3, 'D', 4, 'E', 5, 'F', 6, 'G', 7, 'H', 8]

while True:
    try:
        numero = int(input('Digite um número de 1 a 8: '))
        if str(numero) not in '12345678':
            if len(str(numero)) != 1:
                pass
        else:
            break
    except ValueError:
        print('Digite um número!')

while True:
    letra = str(input('Digite uma letra de A a H: ')).upper()
    if letra not in 'ABCDEFGH':
        if len(letra) != 1:
            pass
    else:
        break

letra = lista[lista.index(letra) + 1]

if

#print(f'O número dessa posição é {numero * letra}')
'''
