from sys import argv
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
from random import choice, randint
from os import listdir, system
from urllib.request import urlretrieve

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir=perfis/perfil{argv[1]}')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )

    def access(self, site):
        self.chrome.get(site)

    def out(self):
        self.chrome.quit()

    def click_select(self, element, item):
        try:
            select_element = self.chrome.find_element_by_id(element)
            select_object = Select(select_element)
            select_object.select_by_visible_text(item)
        except:
            print(f'Erro ao clicar no elemento {item}')

    def click_select_selector(self, element, item):
        select_element = self.chrome.find_element_by_css_selector(element)
        select_object = Select(select_element)
        select_object.select_by_visible_text(item)

    def click_input_id(self, button):
        try:
            btn = self.chrome.find_element_by_id(button)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {button}')

    def click_input_text(self, element):
        btn = self.chrome.find_element_by_link_text(element)
        btn.click()

    def click_input_selector(self, button):
        btn = self.chrome.find_element_by_css_selector(button)
        btn.click()

    def add_image(self, input, image):
        btn = self.chrome.find_element_by_css_selector(input)
        btn.send_keys(image)

    def write(self, element, text):
        btn = self.chrome.find_element_by_id(element)
        btn.send_keys(text)

    def clear(self, element):
        btn = self.chrome.find_element_by_id(element)
        btn.clear()

    def get_text(self, element):
        text = self.chrome.find_element_by_id(element).text
        return text

    def get_text_xpath(self, element):
        try:
            text = self.chrome.find_element_by_xpath(element).text
            return text
        except:
            return ''

    def get_atrib_xpath(self, element):
        try:
            atrib = self.chrome.find_element_by_xpath(element)
            return atrib.get_attribute('src')
        except:
            return ''

    def roll(self, top):
        self.chrome.execute_script(f"window.scrollTo(0, {top})")

    def get_description(self):
        option1 = ['Vendo veículo completo com urgência']
        option2 = ['Nunca batido', 'Sem sinistro']
        ipva = 'IPVA 2021 pago'
        number = 'Para mais informações entre em contato comigo Vinícius Alves via WhatsApp (61) 93500-0935'
        description = f'{choice(option1)}\n{choice(option2)}\n{ipva}\n{number}'
        return description

if __name__ == '__main__':
    system('clear')
    url_car = input('URL: ')
    code = input('Código: ')
    url_olx_base = 'https://www2.olx.com.br/ai/form/0/'
    url_olx = url_olx_base + code
    chrome = ChromeAuto()
    chrome.access(url_car)
    sleep(1)
    print('Foi')
    number = 1
    while True:
        url = chrome.get_atrib_xpath(f'//*[@id="content"]/div[2]/div/div[2]/div[1]/div[37]/div/div/div/div[2]/div/div[1]/div[{number}]/img')
        if url != '':
            urlretrieve(url, f'images/img{number}.jpg')
            number += 1
        elif (url == ''):
            break

    brand = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[3]/div/div[2]/a')
    size_brand = len(brand.split())
    tot_model = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[2]/div/div[2]/a').split()
    model = tot_model[size_brand]
    version = ' '.join(tot_model[size_brand:])
    version_name = ' '.join(tot_model[size_brand + 1:size_brand + 3])
    name = brand.split()[-1].capitalize() + ' ' + model.capitalize() + ' ' + version_name
    description = chrome.get_description()
    year = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[5]/div/div[2]/a')
    gearbox = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[9]/div/div[2]/span[2]')
    fuel = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[8]/div/div[2]/a')
    steering = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[10]/div/div[2]/span[2]')
    motor_power = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[7]/div/div[2]/span[2]')
    car_type = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[4]/div/div[2]/span[2]')

    number1 = randint(8, 10)
    if (number1 < 10):
        number2 = randint(0, 9)
    elif (number1 == 10):
        number2 = 0        
    number_str = f'{number1}.{number2}'
    number = float(number_str)
    subyear = 2021 - int(year)
    mileage = int((subyear * number) * 1000)

    doors = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[12]/div/div[2]/span[2]')

    n = 1
    array_itens = []
    while True:
        item = chrome.get_text_xpath(f'//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[5]/div[2]/div[2]/div[{n}]/div/span')
        if (item != ''):
            array_itens.append(item)
            n += 1
        elif (item == ''):
            break

    color = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[31]/div/div/div/div[4]/div[11]/div/div[2]/span[2]')
    price = chrome.get_text_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div[17]/div/div/div[1]/div[2]/h2')

    chrome.access(url_olx)
    chrome.click_input_id('cookie-notice-ok-button')
    chrome.click_input_id('category_item-2000')
    chrome.click_input_id('category_item-2020')
    chrome.clear('input_subject')
    chrome.write('input_subject', name)
    chrome.clear('input_body')
    chrome.write('input_body', description)
    sleep(1)
    chrome.write('tag', 'OLX1234')
    chrome.click_select('vehicle_brand', brand)
    chrome.click_select('vehicle_model', model)
    chrome.click_select_selector('#regdate > #regdate', year)
    sleep(1)
    chrome.click_select('vehicle_version', version)
    chrome.click_select('gearbox', gearbox)
    chrome.click_select('fuel', fuel)
    chrome.click_select('car_steering', 'Hidráulica')
    chrome.click_select('motorpower', motor_power)
    chrome.click_select('cartype', car_type)
    chrome.write('mileage', mileage)
    chrome.click_select('doors', doors)
    chrome.click_select('end_tag', '4')

    list_features = ['Air bag', 'Alarme', 'Ar condicionado', 'Trava elétrica', 'Vidro elétrico', 'Som', 'Sensor de ré', 'Câmera de ré', 'Blindado', 'Direção hidráulica']
    list_numbers = []

    for number, item in enumerate(list_features):
        if (item in array_itens):
            list_numbers.append(number)

    for number in list_numbers:
        chrome.click_input_id(f'car_features{number}')

    chrome.click_select('exchange', 'Não')
    chrome.click_select('carcolor', color)
    chrome.click_input_id('financial1')
    chrome.click_select('owner', 'Sim')
    chrome.clear('price')
    chrome.write('price', price)
    print(price)

    images = listdir(f'images')
    name = name.replace('/', ' ')
    print(name)
    for image in images:
        chrome.add_image('#group-image-container > div.ads-forms__image-drag-and-drop > div.image-container__box > input', f'images/{image}')