print(30 * '=')
print('{:^30}'.format('Banco Central'))
print(30 * '=')

valor = int(input('Digite o valor a ser sacado: R$'))

cedula = 50
totalCedula = 0

while True:
    if valor >= cedula:
        valor -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if valor == 0:
            break