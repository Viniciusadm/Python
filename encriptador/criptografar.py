from random import randint, choice

class Criptografar:
	def __init__(self):
		self.alfabeto = [x for x in 'u¬{§5t)rd#/[m]!-ª94p0cbkso2i_lz8n,qa|}wºj@;*v%=h?:3e1`7y´xf6$g(.']
		self.cifra = randint(1, 64)
		self.espacos = ['±', '¼', '®', '♪', 'æ']
		self.simbolosAntesDaCifra = ['┼', '«', '╣', '~', '⌂']
		self.simbolosDepoisDaCifra = ['»', '╝', 'ƒ', '┤', '^']
		self.letras = []
		self.letrasEmbaralhadas = []
		self.letrasJuntas = []

	def receberFrase(self):
		self.frase = str(input('Frase a ser codificada: ')).lower().strip()

	def separarPalavras(self):
		self.frase = self.frase.split()
		if len(self.frase) > 1:
			self.frase.insert(1, choice(self.espacos))
			self.frase.insert(0, self.frase[-1])
			self.frase.pop(-1)
			self.frase = ' '.join(self.frase)
		else:
			self.frase = ' '.join(self.frase)

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def criptarFrase(self):
		for self.letra in self.letras:
			if self.letra not in ' ':
				if self.letra in self.alfabeto:
					if self.alfabeto.index(self.letra) + self.cifra >= 64:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 64
						self.letrasEmbaralhadas.append(self.alfabeto[self.index])
					else:
						self.letrasEmbaralhadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
				else:
					self.letrasEmbaralhadas.append(self.letra)
			else:
				self.letrasEmbaralhadas.append(choice(self.espacos))

	def inserirIndice(self):
		self.posicaoAleatoria = randint(0, len(self.letrasEmbaralhadas) - 1)
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria, f'{choice(self.simbolosAntesDaCifra)}{64 - self.cifra}')
		self.letrasEmbaralhadas.insert(self.posicaoAleatoria + 2, choice(self.simbolosDepoisDaCifra))
		
	def adicionarAleatorio(self):
		self.letrasEmbaralhadas.insert(len(self.letrasEmbaralhadas), choice(self.alfabeto + self.espacos + self.simbolosAntesDaCifra + self.simbolosDepoisDaCifra))

	def juntarLista(self):
		self.letrasJuntas = ''.join(self.letrasEmbaralhadas)

	def reverterFrase(self):
		self.letrasJuntas = self.letrasJuntas[::-1]

	def mostraPalavra(self):
		print(self.letrasJuntas)

	def main(self):
		self.receberFrase()
		self.separarPalavras()
		self.criarLista()
		self.criptarFrase()
		self.inserirIndice()
		self.adicionarAleatorio()
		self.juntarLista()
		self.reverterFrase()
		self.mostraPalavra()

iniciar = Criptografar()
iniciar.main()