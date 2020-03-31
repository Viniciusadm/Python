nome = str(input('Digite o seu nome completo: ')).strip().upper().split()
resposta = 'SILVA' in nome
if resposta == True:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')
