while True:
	frase = str(input('Digite uma frase: ')).strip()
	if len(frase.split()) < 2:
		pass
	else:
		break

fraseQuebrada = frase.split()

for palavra in fraseQuebrada:
		for letra in palavra:
			if letra in '"!@#$%*()_+-=§{[}]?/°;:><':
				fraseQuebrada.remove(palavra)
				break

maiorPalavra = fraseQuebrada[0]

for palavra in fraseQuebrada:
	if len(palavra) > len(maiorPalavra):
		maiorPalavra = palavra

print(f'A maior palavra é {maiorPalavra}')