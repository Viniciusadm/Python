class CifraCesar:
	def __init__(self):
		self.alfabeto = [x for x in 'k8ocdn0m16jxbre7t39pwhsvqzau4fy igl53']
		self.letras = []
		self.letrasEmbaralhadas = []
		self.letrasJuntas = []

	def receberFrase(self):
		self.frase = str(input('Digite uma frase: ')).lower()
	
	def receberCifra(self):
		try:
			self.cifra = int(input('Digite o valor da cifra: '))
		except ValueError:
			print('Digite um número')
			self.receberCifra()

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def criptarFrase(self):
		for self.letra in self.letras:
			if self.letra in self.alfabeto:
				if self.alfabeto.index(self.letra) + self.cifra >= 36:
					if self.cifra >= 36:
						self.index = (self.cifra + self.alfabeto.index(self.letra)) % 36
						self.letrasEmbaralhadas.append(self.alfabeto[self.index])
					else:
						self.index = self.alfabeto.index(self.letra) + self.cifra - 36
						self.letrasEmbaralhadas.append(self.alfabeto[self.index])
				else:
					self.letrasEmbaralhadas.append(self.alfabeto[self.alfabeto.index(self.letra) + self.cifra])
			else:
				self.letrasEmbaralhadas.append(self.letra)

	def inserirIndice(self):
		if self.cifra > 36:
			self.cifra %= 36

	def juntarLista(self):
		self.letrasJuntas = ''.join(self.letrasEmbaralhadas)
		print(f'{self.letrasJuntas} + {self.cifra}')

	def main(self):
		self.receberFrase()
		self.receberCifra()
		self.criarLista()
		self.criptarFrase()
		self.receberIndice()
		self.juntarLista()

iniciar = CifraCesar()
iniciar.main()