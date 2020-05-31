from os import system

class Criptografar:
	def __init__(self):
		self.alfabeto = [x for x in 'abcdefghijklmnopqrstuvwxyz']
		self.letras = []
		self.letrasTrocadas = []

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
		self.receberFrase()
		self.receberCifra()
		self.criarLista()
		self.criptarFrase()
		self.juntarLetras()

class Descriptografar:
	def __init__(self):
		self.alfabeto = [x for x in 'abcdefghijklmnopqrstuvwxyz']
		self.frasesDescriptografadas = []
		self.letras = []
		self.letrasTrocadas = []
		self.letrasTrocadasJuntas = []

	def receberFrase(self):
		self.frase = str(input('Digite uma frase: ')).lower()

	def criarLista(self):
		for self.letra in self.frase:
			self.letras.append(self.letra)

	def juntarLetras(self):
		self.letrasTrocadasJuntas = ''.join(self.letrasTrocadas)
		self.letrasTrocadas = []

	def adcionarLista(self):
		self.frasesDescriptografadas.append(self.letrasTrocadasJuntas)
		self.letrasTrocadasJuntas = []

	def criptarFrase(self):
		for self.cifra in range(1, 26):
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
			self.juntarLetras()
			self.adcionarLista()

	def mostrarLista(self):
		for c, d in enumerate(self.frasesDescriptografadas):
			if c + 1 != len(self.frasesDescriptografadas):
				print(d, end='\n')
			else:
				print(d)

	def main(self):
		self.receberFrase()
		self.criarLista()
		self.criptarFrase()
		self.mostrarLista()

class MenuInicial:
	def __init__(self):
		self.criptografia = Criptografar()
		self.descriptografia = Descriptografar()

	def menu(self):
		print('Menu Inicial')
		print('01: Criptografar')
		print('02: Descriptografar')
		print('03: Sair')
		while True:
			try:
				self.resposta = int(input('Opção: '))
			except:
				system('clear')
				print('Opção invalida\n')
				self.menu()
			if self.resposta == 1 or self.resposta == 2 or self.resposta == 3:
				break
			else:
				print('Opção invalida')

	def respostas(self):
		if self.resposta == 1:
			self.criptografia.main()
		if self.resposta == 2:
			self.descriptografia.main()
		if self.resposta == 3:
			pass

	def main(self):
		system('clear')
		self.menu()
		self.respostas()

iniciar = MenuInicial()
iniciar.main()