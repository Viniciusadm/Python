print(30 * '=')
print('{:^30}'.format('Banco Central'))
print(30 * '=')
valor = int(input('Digite o valor a ser sacado: R$'))

nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = nota1 = 0

while valor >= 100:
    nota100 = nota100 + 1
    valor = valor - 100
while valor >= 50:
    nota50 = nota50 + 1
    valor = valor - 50
while valor >= 20:
    nota20 = nota20 + 1
    valor = valor - 20
while valor >= 10:
    nota10 = nota10 + 1
    valor = valor - 10
while valor >= 5:
    nota5 = nota5 + 1
    valor = valor - 5
while valor >= 2:
    nota2 = nota2 + 1
    valor = valor - 2
while valor >= 1:
    nota1 = nota1 + 1
    valor = valor - 1

if nota100 != 0:
    print(f'Total de {nota100} cédulas de R$100')
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota5 != 0:
    print(f'Total de {nota5} cédulas de R$5')
if nota2 != 0:
    print(f'Total de {nota2} cédulas de R$2')
if nota1 != 0:
    print(f'Total de {nota1} cédulas de R$1')
