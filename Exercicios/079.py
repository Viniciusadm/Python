numerosLista = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in numerosLista:
        numerosLista = numerosLista + [numero]
        print('Valor adcionado com sucesso')
    else:
        print('Valor duplicado não será adcionado')
    resposta = str(input('Você deseja continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

numerosLista.sort()

print('A lista de números digitados em ordem é ', end='')

for contador in range(0 ,len(numerosLista)):
    if contador != len(numerosLista) -1:
        print(numerosLista[contador], end=' - ')
    else:
        print(numerosLista[contador])