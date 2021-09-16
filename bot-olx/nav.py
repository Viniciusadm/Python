from selenium import webdriver
from sys import argv

class ChromeAuto:
    def __init__(self):
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir=perfis/perfil{argv[1]}')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )

if __name__ == '__main__':
    chrome = ChromeAuto()
