from random import randint

contador = soma = 0

print(9 * '=-')
print('Par ou Ímpar')
print(9 * '=-')

while True:
    numero = int(input('Diga um valor: '))
    imparPar = str(input('Par ou ímpar? [P/I] ')).upper().strip()
    sorteado = randint(1, 11)
    soma = sorteado + numero
    print(f'Você jogou {numero} e o computador jogou {sorteado}')
    if imparPar == 'P' and soma % 2 == 0 or imparPar == 'I' and soma % 2 != 0:
        contador += 1
    else: 
        break
print(f'Game Over! Você venceu {contador} vez(es)')
