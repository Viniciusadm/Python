numerosLista = []
numerosListaPares = []
numerosListaImpares = []

while True:
    numerosLista.append(int(input('Digite um número: ')))
    resposta = str(input('Você deseja continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

for contador in numerosLista:
    if contador % 2 == 0:
        numerosListaPares.append(contador)
    else:
        numerosListaImpares.append(contador)

print(f'Os valores da lista são ', end='')

for contador in range(0 ,len(numerosLista)):
    if contador != len(numerosLista) -1:
        print(numerosLista[contador], end=' - ')
    else:
        print(numerosLista[contador])

print(f'Os valores pares da lista são ', end='')

for contador in range(0 ,len(numerosListaPares)):
    if contador != len(numerosListaPares) -1:
        print(numerosListaPares[contador], end=' - ')
    else:
        print(numerosListaPares[contador])

print(f'Os valores impares da lista são ', end='')

for contador in range(0 ,len(numerosListaImpares)):
    if contador != len(numerosListaImpares) -1:
        print(numerosListaImpares[contador], end=' - ')
    else:
        print(numerosListaImpares[contador])