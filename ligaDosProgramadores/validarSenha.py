terNumero = terCaractereEspecial = terEspaco = numeroCaracteres = False

senha = str(input('Digite sua senha: '))

if len(senha) >= 5 and len(senha) <= 10:
	numeroCaracteres = True
if numeroCaracteres != True:
	print('A senha deve conter de 5 a 10 caracteres')

for letra in senha:
	if letra in '0123456789':
		terNumero = True
		break
if terNumero != True:
	print('A senha deve conter pelo menos um número')

for letra in senha:
	if letra in '!@#$%&*+-_':
		terCaractereEspecial = True
if terCaractereEspecial != True:
	print('A senha deve conter pelo menos um caracteres especial')

if senha.count(' ') == 0:
	terEspaco = True
if terEspaco != True:
	print('A senha não pode conter espaços')

if numeroCaracteres and terNumero and terCaractereEspecial and terEspaco:
	print('Senha cadastrada com sucesso')