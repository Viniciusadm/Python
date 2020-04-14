def contagemCrescente():
    print(30 * '=')
    print('Contagem de 1 a 10 de 1 em 1')
    for c in range(1, 11):
        if c < 10:
            print(c, end=', ')
        else:
            print(c)

def contagemDecrescente():
    print(30 * '=')
    print('Contagem de 10 a 0 de 2 em 2')
    for c in range(10, -1, -2):
        if c != 0:
            print(c, end=', ')
        else:
            print(c)
    print(30 * '=')

def contagemPersonalizada(inicio, fim, passo):
    print(30 * '=')
    if passo == 0:
        passo = 1
    if inicio < fim:
        print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
        for c, d in enumerate(range(inicio, fim + 1, passo)):
            if c + 1 != len(range(inicio, fim + 1, passo)):
                print(d, end=', ')
            else:
                print(d)
        print(30 * '=')
    else:
        if passo > 0:
            passo *= -1
        if passo < 0:
            lista = list()
            lista.append(str(passo))
        print(f'Contagem de {inicio} a {fim} de {lista[0][1:]} em {lista[0][1:]}')    
        for c, d in enumerate(range(inicio, fim - 1, passo)):
            if c + 1 != len(range(inicio, fim -1, passo)):
                print(d, end=', ')
            else:
                print(d)
        print(30 * '=')

contagemCrescente()

contagemDecrescente()

print('Contagem personalizada')
inicioInput = int(input('Inicio: '))
fimInput = int(input('Fim: '))
passoInput = int(input('Passo: '))

contagemPersonalizada(inicioInput, fimInput, passoInput)