numero = soma = contador = 0
while numero != 999:
    numero = int(input('Digite um número [999 pra parar]: '))
    if numero == 999:
        break
    soma+=numero
    contador+=1
print(f'A soma dos {contador} números digitados é {soma}')