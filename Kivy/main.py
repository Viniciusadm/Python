import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class FirstLayout(BoxLayout):
    def texto(self):
        self.ids.Tela.text = 'Olá, Mundo!'

class CalculadoraRPG(App):
    def build(self):
        return FirstLayout()

CalculadoraRPG().run()