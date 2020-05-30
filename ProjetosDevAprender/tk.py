from tkinter import *

altura = 500
largura = 500

def func():
    print(f'{largura}x{altura}')

menuInicial = Tk() #Coisa o objeto

menuInicial.title('Jogo da Advinhação') #Define título pra tela
menuInicial.iconbitmap('') #Deifine icone da tela
menuInicial['bg'] = '#666666' #Define cor pro fundo

#Define largura e altura da tela
larguraTela = menuInicial.winfo_screenwidth()
alturaTela = menuInicial.winfo_screenheight()

#Define tamanho e posição pra tela
menuInicial.geometry(f'{largura}x{altura}+{int(larguraTela / 2 - largura / 2)}+{int(alturaTela / 2 - altura / 2)}')

menuInicial.minsize(250, 250) #Define o tamanho minimo pro tamanho da tela
menuInicial.maxsize(700, 700) #Define o tamanho máximo pra tela
menuInicial.state('normal') #Iniciar com a tela no maximizada: withdraw, minimizada: iconic
menuInicial.resizable(True, True) #Define se a tela pode mudar de tamanho

#Coisa um botão
btn = Button(
    menuInicial,
    text = 'Executar', #Texto exibido
    command = func #Comando ao apertar o botão
).grid(row = 1, sticky = W)

#Coisa uma label
lbl = Label(
    menuInicial,
    text = 'Olá, Mundo!', #Texto exibido
    bg = '#aaaaaa', #Cor do fundo
    fg = 'blue', #Cor da letra
    font = 'Arial 20 bold italic', #Fonte do texto
    width = '0', #Largura
    height = '0', #Altura
    state = 'normal', #Nem sei
    bd = '1', #Tamanho da borda
    relief = 'solid', #Tipos de borda: solid, groove, flat, raised, sunken e ridge
    anchor = CENTER, #Posição do texto: n, ne, e, se, s, sw, w, nw, e center
    padx = 0, #Padding posição x
    pady = 0, #Padding posição y
    justify = CENTER #Justificação do texto
).grid(row = 0, sticky = W)

#Coisa uma caixa de texto
texto = Entry(menuInicial)
texto.grid(columnspan = 2)
texto.focus()

menuInicial.mainloop() #Impõe um loop pra tela