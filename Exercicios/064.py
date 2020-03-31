numero = 0
soma = -999
contador = -1
while numero != 999:
    numero = int(input('Digite um número [999 pra parar]: '))
    soma+=numero
    contador+=1
print(f'A soma dos {contador} números digitados é {soma}')