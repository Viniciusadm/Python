from time import sleep

def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    if inicio < fim:
        sleep(1)
        for c, d in enumerate(range(inicio, fim + 1, passo)):
            if c + 1 != len(range(inicio, fim + 1, passo)):
                print(d, end=', ', flush=True)
                sleep(0.5)
            else:
                print(d)
        print(30 * '=')
    else:
        for c, d in enumerate(range(inicio, fim - 1, -passo)):
            if c + 1 != len(range(inicio, fim - 1, -passo)):
                print(d, end=', ', flush=True)
                sleep(0.5)
            else:
                print(d)
        print(30 * '=')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('Contagem personalizada')
inicioInput = int(input('Inicio: '))
fimInput = int(input('Fim: '))
passoInput = int(input('Passo: '))

contagem(inicioInput, fimInput, passoInput)