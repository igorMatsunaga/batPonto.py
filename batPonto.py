from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
import time

username = 'nomeusuario'
password = 'senha'
agora = datetime.now()
td = '2018-04-29 07:30:01.804925'
td1 = '2018-04-30 11:30:01.804925'
td2 = '2018-04-30 12:31:01.804925'
td3 = '2018-04-30 16:35:01.804925'

def batPonto():
    # Criar Instancia
    driver = webdriver.Chrome('C:\\Users\\igor\\Desktop\\backup\\chromedriver_win32//chromedriver')
    # Abrir Pagina
    driver.get('http://srv-vib01:8082/sistema/login.xhtml')
    # Maximizar janela
    driver.maximize_window()
    # Instancia formularios
    elem = driver.find_element_by_id("frm:login")
    elem.send_keys(username)
    elem = driver.find_element_by_id("frm:senha")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    # aperta botão
    elem.click()
    # Redireciona Pagina
    driver.get('http://srv-vib01:8082/sistema/secured/Registro.xhtml')
    # Instancia botão
    btn = driver.find_element_by_xpath('//*[@id="botaoSalvar"]/span')
    btn.click()

# Condição para tempo
if agora == td or agora == td1 and agora == td2 and agora == td3:
    batPonto()

else:
    time.sleep(14400)
