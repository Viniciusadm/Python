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
        if letras == '+' or letras == '-':
            break
    dado = dado[contador: ]
    lista2 = dado
    lista = ''.join(lista)
    dado = int(lista)
    lista = []
    for contador, letras in enumerate(lista2):
        listaSoma = []
        listaSubtracao = []
        somaSoma = 0
        subtracao = 0
        if letras == '+':
            lista2 = lista2[contador + 1: ]
        if letras.isnumeric() == True:
           lista.append(letras)
        for letras in lista:
            somaSoma += int(letras)
        lista = []
        if letras == '-':
            lista2 = lista2[contador + 1: ]
        if letras.isnumeric() == True:
           lista.append(letras)
        for letras in lista:
            subtracao += int(letras)
    for contador in range(1, quantidade + 1):
        dados.append(randint(1, dado))
    for contador in dados:
        soma += contador
    for contador in dados:
        print(f'{contador}', end=' ')
    print(f'({soma + somaSoma - subtracao})')
    dados = []
    soma = 0
    lista = []