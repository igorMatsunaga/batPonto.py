import time
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

username = 'igor'
password = 'Abril'
agora = datetime.now()
td = '2018-04-29 22:09:01.804925'
td1 = '2018-04-30 22:10:01.804925'
td2 = '2018-04-30 22:11:01.804925'
td3 = '2018-04-30 22:12:01.804925'


driver = webdriver.Chrome('C:\\Users\\Admin\\Desktop\\beckup//chromedriver')

def batPonto():

    driver.get('https://url')
    driver.maximize_window()
    elem = driver.find_element_by_id("j_username")
    elem.send_keys(username)
    elem = driver.find_element_by_id("j_password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_css_selector(".input.textInput")
    elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
    elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
    elem.click()

    return



if (td != agora):
    while False:
        time.sleep(td)
    else:
        batPonto()

        if (td2 != agora):
            while False:
                time.sleep(td2)
            else:
                batPonto()

                if (td3 != agora):
                    while False:
                        time.sleep(td3)
                    else:
                        batPonto()


print(agora)

driver.close()