#AUTOMATIZACION DE BUSQUEDA DE UN PRODUCTO EN AMAZON
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def buscar_en_amazon(product):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size = 1020, 1200")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx/")

    buscador = navegador.find_element(By.NAME, "field-keywords")
    buscador.send_keys(product)
    time.sleep(3)

    btnsearch = navegador.find_element(By.ID, "nav-search-submit-button")
    btnsearch.click()
    time.sleep(3)

    navegador.save_screenshot("img_amazon.png")
    navegador.quit()

# Para utilizar la función, simplemente llama a buscar_en_amazon con el producto que desees buscar
product = str(input("Ingrese el producto que quiere buscar:"))
buscar_en_amazon(product)

#time.sleep(10)