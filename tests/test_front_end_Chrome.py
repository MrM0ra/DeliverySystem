from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser=webdriver.Chrome('/Users/c/Downloads/chromedriver')

#browser.get('http://www.youtube.com')
browser.get('http://127.0.0.1:5000/')

time.sleep(5)

# encuentra el elemento que tenga link de texto
browser.find_element_by_link_text('Ingresar')
#asigna el elemento a una variable
elem=browser.find_element_by_link_text('Ingresar')
#Hace click en el elemento
elem.click()

time.sleep(5)

# encuentra el elemento con el id pasado
login_user = browser.find_element_by_id('tx_user')
# escribe el parametro pasado en el campo encontrado
login_user.send_keys('admin')
# encuentra el elemento con el id pasado
login_pass = browser.find_element_by_id('txtPassword')
# escribe el parametro pasado en el campo encontrado
login_pass.send_keys('admin')

#login_pass.send_keys(Keys.ENTER)

# encuentra el elemento con el id pasado
login = browser.find_element_by_id('submit')
#Hace click en el elemento
login.click()

time.sleep(5)
