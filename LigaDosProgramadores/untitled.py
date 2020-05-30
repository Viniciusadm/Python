class CifraCesar:
	def __init__(self):
		self.alfabeto = [x for x in 'abcdefghijklmnopqrstuvwxyz']
		self.letras = []
		self.letrasTrocadas = []

	def receberValores(self):
		self.frase = str(input('Digite uma frase: ')).lower()
		self.cifra = int(input('Digite o valor da cifra: '))

	def criptarFrase(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

		for self.letra in self.letras:
			if self.letra in self.alfabeto:
				if self.alfabeto.index(self.letra) + self.cifra >= 26:
					if self.cifra >= 26:
						self.index = (self.cifra + self.alfabeto.index(self.letra)) % 26
						self.letrasTrocadas.append(self.alfabeto[self.index])
					else:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 26
						self.letrasTrocadas.append(self.alfabeto[self.index])
				else:
					self.letrasTrocadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
			else:
				self.letrasTrocadas.append(self.letra)

	def juntarLetras(self):
		self.letrasTrocadasJuntas = ''.join(self.letrasTrocadas)
		print(self.letrasTrocadasJuntas)

	def main(self):
		self.receberValores()
		self.criptarFrase()
		self.juntarLetras()

iniciar = CifraCesar()
iniciar.main()