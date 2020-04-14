aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = str('Aprovado')
elif aluno['Média'] < 7 and aluno['Média'] >= 5:
    aluno['Situação'] = str('Recuperação')
else:
    aluno['Situação'] = str('Reprovado')

for c, d in aluno.items():
    print(f'{c} é igual a {d}')