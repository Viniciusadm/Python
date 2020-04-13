lista = [[]]
contador = int(0)

while True:
    nome = str(input('Nome: '))
    lista[contador].append(nome)
    lista[contador].append([])
    nota1 = float(input('Nota 1: '))
    lista[contador][1].append(nota1)
    nota2 = float(input('Nota 2: '))
    lista[contador][1].append(nota2)
    lista[contador][1].append((nota1 + nota2) / 2)
    resposta = str(input('Deseja continuar? ')).upper()
    if resposta == 'N':
        break
    lista.append([])
    contador += 1

print('No.  Nome      Média')
print(20 * '-')
for c, d in enumerate(lista):
    print(f'{c:<-4}', end=' ')
    print(f'{d[0]:<9}', end=' ')
    print(f'{d[1][2]:.1f}')
print(20 * '-')

while True:
    resposta = int(input('Mostrar notas (-1 interrompe): '))
    while True:
        if resposta <= c:
            break
        else:
            resposta = int(input('''\033[0;31mAluno Invalido! \033[m
Mostrar notas (-1 interrompe): '''))
    if resposta == -1:
        break
    print(f'As notas de {lista[resposta][0]}', end=' ')
    for c, d in enumerate(lista[resposta][1]):
        if c == 0:
            print(d, end=' e ')
        elif c == 1:
            print(d)
