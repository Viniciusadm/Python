frutas = ('Banana', 'Laranja', 'Mexerica', 'Pera', 'Cacau', 'Coco')
frutasMinusculo = frutas

for vogais in frutas:
    print(f'\nNa palavra {vogais} temos as vogais ', end='')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')