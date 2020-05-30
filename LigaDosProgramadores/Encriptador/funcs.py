class Enciptador:
	def __init__(self):
		self.alfabeto = [x for x in 'k8ocdn0m16jxbre7t39pwhsvqzau4fyigl53']
		self.cifra = randint(1, 36)
		self.espacos = ['±', '¼', '®', 'Ø', 'æ']
		self.simbolosAntesDaCifra = ['»', '«', 'ƒ', '~', '⌂']
		self.simbolosDepoisDaCifra = ['┼', '╝', '╣', '┤', '^']
		self.letras = []
		self.letrasEmbaralhadas = []
		self.letrasJuntas = []

	def receberFrase(self):
		self.frase = str(input('Frase a ser codificada: ')).lower()

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def criptarFrase(self):
		for self.letra in self.letras:
			if self.letra not in ' ':
				if self.letra in self.alfabeto:
					if self.alfabeto.index(self.letra) + self.cifra >= 36:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 36
						self.letrasEmbaralhadas.append(self.alfabeto[self.index])
					else:
						self.letrasEmbaralhadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
				else:
					self.letrasEmbaralhadas.append(self.letra)
			else:
				self.letrasEmbaralhadas.append(choice(self.espacos))

	def inserirIndice(self):
		self.posicaoAleatoria = randint(0, len(self.letrasEmbaralhadas) - 1)
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria, f'{choice(self.simbolosAntesDaCifra)}{self.cifra}')
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria + 2, choice(self.simbolosAntesDaCifra))
		
	def juntarLista(self):
		self.letrasJuntas = ''.join(self.letrasEmbaralhadas)
		print(self.letrasJuntas)