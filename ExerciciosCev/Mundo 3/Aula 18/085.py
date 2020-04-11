dado = list()
lista = [[], []]

for c in range(1, 8):
    dado.append(int(input(f'Digite o {c}° número: ')))
    if dado[0] % 2 == 0:
        lista[0].append(dado[0])
    else:
        lista[1].append(dado[0])
    dado.clear()

print('A lista com os números pares é ', end='')
for c, g in enumerate(sorted(lista[0])):
    if len(lista[0]) != c + 1:
        print(g, end=', ')
    else:
        print(g)

print('A lista com os números pares é ', end='')
for c, g in enumerate(sorted(lista[1])):
    if len(lista[1]) != c + 1:
        print(g, end=', ')
    else:
        print(g)