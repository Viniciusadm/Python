numerosLista = []
cont = 0

while True:
    numerosLista.append(int(input('Digite um número: ')))
    resposta = str(input('Você deseja continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

numerosListaContrario = sorted(numerosLista, reverse = True)

print(f'Você digitou {len(numerosLista)} elementos')
print(f'Os valores em ordem decrescente são ', end='')

for contador in range(0 ,len(numerosListaContrario)):
    if contador != len(numerosListaContrario) -1:
        print(numerosListaContrario[contador], end=' - ')
    else:
        print(numerosListaContrario[contador])

if 5 in numerosLista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')