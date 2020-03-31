frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
fraseContrario = frase[-1 :: -1]
print(f'O inverso de {frase} é {fraseContrario}')
if fraseContrario == frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')