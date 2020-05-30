class Desencriptar:
	def __init__(self):
		self.alfabeto = [x for x in 'u¬{§5t)rd#/[m]!-ª94p0cbkso2i_lz8nqa|}wºj@*v%=h?3e1`7y´xf6$g(']
		self.espacos = ['±', '¼', '®', ' ♪', 'æ']
		self.simbolosAntesDaCifra = ['┼', '«', '╣', '~', '⌂']
		self.simbolosDepoisDaCifra = ['»', '╝', 'ƒ', '┤', '^']

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
		print(self.frase)

	def main(self):
		self.receberFrase()
		self.reverterFrase()
		self.inserirEspacos()

iniciar = Desencriptar()
iniciar.main()
