lista = list()
maiorNumero = 0

def maior(numeros):
    gatilho = 0
    for c in numeros:
        if gatilho == 0:
            maiorNumero = c
            gatilho = 1
        if c > maiorNumero:
            maiorNumero = c

    for c, d in enumerate(numeros):
        if c + 1 != len(numeros):
            print(d, end=', ')
        else:
            print(d, end=' ')

    print(f'Foram informados {len(numeros)} valores ao todo')
    print(f'O maior valor informado foi {maiorNumero}')

quantidade = int(input('Quantos números você deseja informar? '))

for c in range(1, quantidade + 1):
    lista.append(int(input(f'Digite o {c}° número: ')))

maior(lista)