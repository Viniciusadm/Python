class Decriptar:
	def __init__(self):
		self.alfabeto = [x for x in 'u¬{§5t)rd#/[m]!-ª94p0cbkso2i_lz8nqa|}wºj@*v%=h?3e1`7y´xf6$g(']
		self.espacos = ['±', '¼', '®', ' ♪', 'æ']
		self.simbolosAntesDaCifra = ['┼', '«', '╣', '~', '⌂']
		self.simbolosDepoisDaCifra = ['»', '╝', 'ƒ', '┤', '^']
		self.letras = []
		self.letrasDesembaralhadas = []

	def receberFrase(self):
		self.frase = str(input('Frase a ser descodificada: ')).lower()

	def reverterFrase(self):
		self.frase = self.frase[::-1]

	def inserirEspacos(self):
		self.frase = self.frase.replace('±', ' ')
		self.frase = self.frase.replace('¼', ' ')
		self.frase = self.frase.replace('®', ' ')
		self.frase = self.frase.replace('♪', ' ')
		self.frase = self.frase.replace('æ', ' ')

	def encontrarSimboloAntesIndice(self):
		self.inicio = self.frase.find('┼')
		if self.inicio != -1:
			pass
		else:
			self.inicio = self.frase.find('«')
			if self.inicio != -1:
				pass
			else:
				self.inicio = self.frase.find('╣')
				if self.inicio != -1:
					pass
				else:
					self.inicio = self.frase.find('~')
				if self.inicio != -1:
					pass
				else:
					self.inicio = self.frase.find('⌂')

	def encontrarSimboloDepoisIndice(self):
		self.final = self.frase.find('»')
		if self.final != -1:
			pass
		else:
			self.final = self.frase.find('╝')
			if self.final != -1:
				pass
			else:
				self.final = self.frase.find('ƒ')
				if self.final != -1:
					pass
				else:
					self.final = self.frase.find('┤')
				if self.final != -1:
					pass
				else:
					self.final = self.frase.find('^')

	def encontrarIndice(self):
		self.cifra = self.frase[self.inicio + 1:self.final - 1]
		self.tamanhoIndice = len(self.cifra)
		self.cifra = int(self.cifra)

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def deletarCaracteresInuteis(self):
		del self.letras[self.inicio]
		del self.letras[self.final - 1]
		if self.tamanhoIndice == 1:
			del self.letras[self.inicio]
		else:
			del self.letras[self.inicio: self.inicio + 2]

	def decriptarFrase(self):
		for self.letra in self.letras:
			if self.letra not in ' ':
				if self.letra in self.alfabeto:
					if self.alfabeto.index(self.letra) + self.cifra >= 60:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 60
						self.letrasDesembaralhadas.append(self.alfabeto[self.index])
					else:
						self.letrasDesembaralhadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
				else:
					self.letrasDesembaralhadas.append(self.letra)
			else:
				self.letrasDesembaralhadas.append(' ')
				
	def juntarLista(self):
		self.letrasJuntas = ''.join(self.letrasDesembaralhadas)
		print(self.letrasJuntas)

	def main(self):
		self.receberFrase()
		self.reverterFrase()
		self.inserirEspacos()
		self.encontrarSimboloAntesIndice()
		self.encontrarSimboloDepoisIndice()
		self.encontrarIndice()
		self.criarLista()
		self.deletarCaracteresInuteis()
		self.decriptarFrase()
		self.juntarLista()

iniciar = Decriptar()
iniciar.main()
