cont = 0
numero = int(input('Digite um número: '))

for c in range(1, numero + 1):
    if numero % c == 0:
        cont += 1

print(numero)
if cont == 3:
    print('É jooj')
else:
    print('Não é jooj')
