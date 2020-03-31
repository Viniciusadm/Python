from random import randint

numerosAleatorios = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))

print('Os números gerados foram: ', end='')
for c in numerosAleatorios:
    print(c, end=' ')

print(f'\nO maior número é o {max(numerosAleatorios)}')
print(f'O menor número é o {min(numerosAleatorios)}')