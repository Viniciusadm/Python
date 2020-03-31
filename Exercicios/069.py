maiorIdade = homens = mulheres = 0
print('Cadastramento de Pessoas')

while True:
    idade = int(input('Idade: '))

    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
        if sexo == 'M' or sexo == 'F':
            break

    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
        homens =+ 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if resposta == 'S' or resposta == 'N':
            break
    if resposta == 'N':
        break

print(f'Total de pessoas maior de idade: {maiorIdade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')