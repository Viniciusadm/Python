listaPessoas = list()
listaMedia = list()
listaMulheres = list()
pessoa = dict()
listaAcimaMedia = list()
media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    listaPessoas.append(pessoa.copy())
    pessoa.clear()
    resposta = str(input('Deseja continuar? ')).upper()
    if resposta == 'N':
        break

for c in range(0, len(listaPessoas)):
    listaMedia.append(listaPessoas[c]['idade'])
media = (sum(listaMedia)) / len(listaPessoas)

print(45 * '=')

print(f'A) O grupo tem {len(listaPessoas)} pessoas')

if (media - int(media)) != 0:
    print(f'B) A média de idade é de {media:.1f} anos')
else:
    print(f'B) A média de idade é de {media:.0f} anos')

for c in listaPessoas:
    if c['sexo'] == 'F':
        listaMulheres.append(c['nome'])

if len(listaMulheres) != 0:
    print('C) As mulheres cadastradas foram: ', end='')
    for c, d in enumerate(listaMulheres):
        if c + 1 < len(listaMulheres):
            print(d, end=', ')
        else:
            print(d)

for c in listaPessoas:
    if c['idade'] >= media:
        listaAcimaMedia.append(c.copy())

print('D) Lista de pessoas que estão acima da média: ')
for c in listaAcimaMedia:
    for d, e in c.items():
        print(f'{d} = {e};', end=' ')
    print('\n', end='')