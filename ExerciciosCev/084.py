lista = list()
dado = list()
listaMaior = list()
listaMenor = list()
pesoMaior = pesoMenor = gatilho = 0
resposta = 'S'

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))

    if gatilho != 1:
        pesoMaior = dado[1]
        pesoMenor = dado[1]
        gatilho = 1
    else:
        if dado[1] > pesoMaior:
            pesoMaior = dado[1]
        if dado[1] < pesoMenor:
            pesoMenor = dado[1]
    
    lista.append(dado[:])
    dado.clear()
    resposta = str(input('Deseja continuar? ')).upper()

    if resposta == 'N':
        break

print(f'Ao todo, você cadastrou {len(lista)} pessoas')

for c in lista:
    if c[1] == pesoMaior:
        listaMaior.append(c[0])
    if c[1] == pesoMenor:
        listaMenor.append(c[0])

print(f'O maior peso foi de {pesoMaior:.2f}Kg. Peso de', end=' ')
for h, g in enumerate(listaMaior):
    if len(listaMaior) != h + 1:
        print(g, end=', ')
    elif len(listaMaior) == h + 1:
        print(f'{g}')

print(f'O menor peso foi de {pesoMenor:.2f}Kg. Peso de', end=' ')
for h, g in enumerate(listaMenor):
    if len(listaMenor) != h + 1:
        print(g, end=', ')
    elif len(listaMenor) == h + 1:
        print(f'{g}')