from datetime import date
pessoa = dict()
anoAtual = date.today().year

pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = anoAtual - int(input('Ano de Nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho: '))

if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] - (anoAtual - pessoa['Idade'])) + 35

print(40 * '=')
for c, d in pessoa.items():
    print(f'{c} tem o valor {d}')