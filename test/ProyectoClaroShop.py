import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.claroshop.com/")
time.sleep(10)

menu = navegador.find_element(By.XPATH, "//*[@id='__next']/div[1]/header/div[1]/div[2]/div/nav[2]/ul[1]/li[2]/a")
menu.click()
time.sleep(20)

data = {"Producto": [], "Precio Actual": [], "Precio Anterior": [], "Forma de pago": []}


soup = BeautifulSoup(navegador.page_source, "html.parser")
lista_divs = soup.find_all(name="div", attrs={"class": "tarjeta-producto-pagos filtro"})

for i in lista_divs[1:]:
    productname = i.find("h3", attrs={"class": "product-name"})
    actualprice = i.find("p", attrs={"class": "sale-price-product"})
    oldprice = i.find("p", attrs={"class": "price-product"})
    payment = i.find("div", attrs={"class": "meses-telmex"})

    data["Producto"].append(productname.text)
    data["Precio Actual"].append(actualprice.text if actualprice else 0)
    data["Precio Anterior"].append(oldprice.text if oldprice else 0)
    data["Forma de pago"].append(payment.text if payment else "NA")

navegador.close()

data_df = pd.DataFrame(data)
data_df.to_csv("ClaroShop.csv")


