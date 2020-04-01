#Importação de Bibliotecas
from random import randint

#Declaração de Variáveis
dados = []
lista = []
soma = 0

while True:
    dado = str(input('Dado: '))
    for contador, letras in enumerate(dado):
        if letras.isnumeric() == True:
            lista.append(letras)
        else:
            break
    dado = dado[contador: ]
    lista = ''.join(lista)
    quantidade = int(lista)
    lista = []

    for contador, letras in enumerate(dado):
        if letras.isnumeric() == True:
            lista.append(letras)
    dado = dado[contador: ]
    lista = ''.join(lista)
    dado = int(lista)

    for contador in range(1, quantidade + 1):
        dados.append(randint(1, dado))
    for contador in dados:
        soma += contador
    for contador in dados:
        print(f'{contador}', end=' ')
    print(f'({soma})')
    dados = []
    soma = 0
    lista = []