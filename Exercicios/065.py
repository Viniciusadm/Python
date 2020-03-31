contador = soma = media = maior = menor = 0

numero = int(input('Digite um número: '))
maior = numero
menor = numero
contador += 1
soma += numero
resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

while resposta == 'S':
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    contador += 1
    soma += numero
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

print(f'Você digitou {contador} números e a média foi {soma / contador}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')