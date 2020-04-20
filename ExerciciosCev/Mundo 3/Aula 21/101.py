from datetime import date
anoAtual = date.today().year

def voto(ano):
    if anoAtual - nascimento <= 15:
        return 'Não vota'
    elif anoAtual - nascimento >= 16 and anoAtual - nascimento <= 17:
        return 'Voto opcional'
    else:
        return 'Voto obrigatório'

nascimento = int(input('Ano de nascimento: '))
print(f'Com {anoAtual - nascimento} anos: {voto(nascimento)}')