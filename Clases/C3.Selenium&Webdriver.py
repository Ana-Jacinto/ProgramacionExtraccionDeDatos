#AUTOMATIZAR UN LOGIN A FACEBOOK

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#Controlar todas las configuraciones de un navgador ejem. cookies
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#CREAR OBJETO
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://es-la.facebook.com/")

#ENCONTRAR ELEMENTO PARA INGRESAR DATOS
#BY = Buscar por..
Email = navegador.find_element(By.NAME, "email")
#ESCRIBIR DENTRO DEL ELEMENTO ENCONTRADO
Email.send_keys("usuario@gmail.com")
time.sleep(2)
#print(Email)

Password = navegador.find_element(By.NAME, "pass")
Password.send_keys("****")
time.sleep(2)
#print(Password)

navegador.save_screenshot("img_test.png")

#PARA DAR CLICK EN INICIAR CUENTA
btnlogin = navegador.find_element(By.NAME, "login")
btnlogin.click()

print(navegador.title)

#PAUSA PARA LA PAGINA QUE SE ABRE Y NO SE CIERRE AL INSTANTE
time.sleep(5)