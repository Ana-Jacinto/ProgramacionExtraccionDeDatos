#AUTOMATIZACION DE BUSQUEDA DE UN PRODUCTO EN AMAZON RECOLECTANDO LOS RESULTADOS EN UN DF
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


def configure_driver():
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size = 1020, 1200")
    return webdriver.Chrome(service=s, options=opc)


def search_amazon_product(driver, product):
    driver.get("https://www.amazon.com.mx/")
    time.sleep(10)

    buscador = driver.find_element(By.NAME, "field-keywords")
    buscador.send_keys(product)
    time.sleep(3)

    btnsearch = driver.find_element(By.ID, "nav-search-submit-button")
    btnsearch.click()
    time.sleep(3)


def scrape_product_results(driver, pages):
    data = {"Producto": [], "Raiting": [], "Precio": [], "Fecha de Entrega": []}

    for _ in range(pages):
        btnnext = driver.find_element(By.CSS_SELECTOR, ".s-pagination-next")
        btnnext.click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        lista_divs = soup.find_all(name="div", attrs={
            "class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})

        for i in lista_divs:
            productname = i.find("span", attrs={"class": "a-size-base-plus a-color-base a-text-normal"})
            raiting = i.find("span", attrs={"class": "a-size-base puis-bold-weight-text"})
            price = i.find("span", attrs={"a-price-whole"})
            date = i.find("span", attrs={"a-color-base a-text-bold"})

            data["Producto"].append(productname.text)
            data["Raiting"].append(raiting.text if raiting else 0)
            data["Precio"].append(price.text if price else 0)
            data["Fecha de Entrega"].append(date.text if date else "Sin Fecha de Entrega")

    return pd.DataFrame(data)

def main():
    product = str(input("Ingrese el producto que quiere buscar: "))
    pages = int(input("¿Cuántas páginas de resultados desea recorrer? "))

    driver = configure_driver()
    search_amazon_product(driver, product)
    datadf = scrape_product_results(driver, pages)
    datadf.to_csv("amazon.csv")

    driver.quit()

main()