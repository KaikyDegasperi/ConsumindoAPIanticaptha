from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Aqui você vai importar o seu tipo de captcha
from anticaptchaofficial.hcaptchaproxyless import *
import time

# Vamos criar um navegador para não precisamos instaciar ou baixar um webdriver

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# criar uma variavel para o link
link = 'url'

# passar o verbo do protocolo http
navegador.get('link')

# no seu navegador ache a div que fica acima do iframe do captcha tente achar id se não achar ByClassName
chave_captcha = navegador.find_element(By.ID, 'idDoSeuElemento').get_attribute('data-sitekey')

# fazendo a cadeia de resolução

# nesse solver tem que usar seu capctha que foi importado

solver = hCaptchaProxyless

# acompanhador de requirimento

solver.set_verbose(1)

# coloque a chave da sua api

solver.set_website_key('suaChave')

resposta = solver.solve_and_return_solution()

if resposta != 0:
    navegador.execute_script(f"document.getElementById('idDoseuElemento').innerHTML = '{resposta}")
    navegador.find_element(By.ID, 'btnEntrar').click()
else:
    print(solver.err_string)

time.sleep(10)

navegador.close()
