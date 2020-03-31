'''numerosLista = []

for c in range(2, 6):
    numero = int(input(f'Digite o {c}° número: '))

    for posicao, lista in enumerate(numerosLista):
        if numero < numerosLista[posicao]:
            numerosLista.insert(posicao, numero)
            print(f'Adcionado na posição {posicao + 1} da lista')
            break
        
        if numero == numerosLista[posicao]:
            numerosLista.insert(posicao, numero)
            print(f'Adcionado na posição {posicao + 1} da lista')
            break

        else:
            numerosLista.append(numero)
            print('Adcionado ao final da lista')
            break

print('A lista de números digitados em ordem é ', end='')

for contador in range(0 ,len(numerosLista)):
    if contador != len(numerosLista) -1:
        print(numerosLista[contador], end=' - ')
    else:
        print(numerosLista[contador])'''

numerosLista = []

for c in range(1, 6):
    numero = int(input(f'Digite o {c}° número: '))

    if c == 1 or numero > numerosLista[-1]:
        numerosLista.append(numero)
    else:
        pos = 0
        while pos < len(numerosLista):
            if numero <= numerosLista[pos]:
                numerosLista.insert(pos, numero)
                break
            pos += 1

print('A lista de números digitados em ordem é ', end='')

for contador in range(0 ,len(numerosLista)):
    if contador != len(numerosLista) -1:
        print(numerosLista[contador], end=' - ')
    else:
        print(numerosLista[contador])