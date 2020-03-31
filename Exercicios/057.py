sexo = str(input('Informe seu sexo [M/F]:')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso')