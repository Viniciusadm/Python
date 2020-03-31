from random import randint
aleatorio = randint(1, 100)
contador = 1

print('Um número de 1 a 100 foi sorteado')
palpite = int(input('Qual o seu palpite? '))

while aleatorio != palpite:
    if aleatorio > palpite:
        palpite = int(input('Tente um número maior: '))
        contador+=1
    if aleatorio < palpite:
        palpite = int(input('Tente um número menor: '))
        contador+=1
print(f'Você acertou o número {aleatorio} em {contador} tentativas')