#AUTOMATIZACION DE BUSQUEDA DE UN PRODUCTO EN AMAZON RECOLECTANDO LOS RESULTADOS EN UN DF
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

def search_amazon(product, pages):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size = 1020, 1200")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(10)

    buscador = navegador.find_element(By.NAME, "field-keywords")
    buscador.send_keys(product)
    time.sleep(3)

    btnsearch = navegador.find_element(By.ID, "nav-search-submit-button")
    btnsearch.click()
    time.sleep(3)

    # Recorrer el número de páginas especificado
    for i in range(pages):
        btnnext = navegador.find_element(By.CSS_SELECTOR, ".s-pagination-next")
        btnnext.click()
        time.sleep(3)

    soup = BeautifulSoup(navegador.page_source, "html.parser")
    lista_divs = soup.find_all(name="div", attrs={"class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})

    data = {"Producto": [], "Raiting": [], "Precio": [], "Fecha de Entrega": []}

    for i in lista_divs:
        productname = i.find("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
        raiting = i.find("span", attrs={"class": "a-size-base puis-bold-weight-text"})
        price = i.find("span", attrs={"a-price-whole"})
        date = i.find("span", attrs={"a-color-base a-text-bold"})

        data["Producto"].append(productname.text)
        data["Raiting"].append(raiting.text if raiting else 0)
        data["Precio"].append(price.text if price else 0)
        data["Fecha de Entrega"].append(date.text if date else "Sin Fecha de Entrega")

    data_df = pd.DataFrame(data)
    data_df.to_csv("amazon.csv")

    navegador.quit()

# Llama a la función con los valores deseados
product = str(input("Ingrese el producto que quiere buscar:"))
pages = int(input("¿Cuántas páginas de resultados desea recorrer?"))

search_amazon(product, pages)
#print(data)

