#Importação de Bibliotecas
from random import randint

#Declaração de Variáveis
dados = []
lista = []
soma = 0
somaSoma = 0
subtracao = 0

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
    listaSoma = dado
    lista = ''.join(lista)
    dado = int(lista)
    listadeSoma = []
    listadeSubtracao = []
    for contador, letras in enumerate(listaSoma):

        if letras == '+':
            listaSoma = listaSoma[contador + 1: ]
            for contadorSoma in listaSoma:
                if listadeSoma == '-':
                    break
                if contadorSoma.isnumeric() == True:
                    listadeSoma.append(contadorSoma)
                    for cont in listadeSoma:
                        somaSoma += int(cont)
                        listadeSoma = []
        if letras == '-':
            listaSoma = listaSoma[contador + 1: ]
            for contadorSubtracao in listaSoma:
                if listadeSubtracao == '+':
                    break
                if contadorSubtracao.isnumeric() == True:
                    listadeSubtracao.append(contadorSubtracao)
                    for cont in listadeSubtracao:
                        subtracao += int(cont)
                        listadeSubtracao = []
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