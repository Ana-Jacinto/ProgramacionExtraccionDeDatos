import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#Controlar todas las configuraciones de un navgador ejem. cookies
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#SELENIUM HACE EL BOOT QUE CONTROLA
#BEAUTIFULSOUP RECOLECTA INFORMACION


#CREAR OBJETO
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("http://www.olympedia.org/statistics/medal/country")

#BUSCAR UN ELEMENTO (ELEMENT)
cmbYear = navegador.find_element(By.NAME, "edition_id")
cmbGender = navegador.find_element(By.NAME, "athlete_gender")

#BUSCAR UNA LISTA (ELEMENTS)
genderOptions = cmbGender.find_elements(By.TAG_NAME, 'option')
yearGroups = cmbYear.find_elements(By.TAG_NAME, 'optgroup')

yearlist = yearGroups[0].find_elements(By.TAG_NAME, 'option')

#CREAR DICCIONARIO
datos = {
    "country":[],
    "year": [],
    "gender": [],
    "gold": [],
    "silver": [],
    "bronze": [],
    "total": []
}

#CICLO PARA SELECCIONAR EL GENERO Y QUE VAYAN CAMBIANDO LOS ANOS.
for gender in genderOptions[1:]:
    gender.click()
    #time.sleep(1)
    for year in yearlist:
        year.click()
        time.sleep(2)

        soup = BeautifulSoup(navegador.page_source, "html.parser")
        tabla = soup.find("table", attrs={"class": "table table-striped"})
        list_rows = tabla.find_all("tr")

        for row in list_rows[1:]:
            datos["gender"].append(gender.text)
            datos["year"].append(year.text)
            values = row.find_all("td")
            datos["country"].append(values[0].text)
            datos["gold"].append(values[2].text)
            datos["silver"].append(values[3].text)
            datos["bronze"].append(values[4].text)
            datos["total"].append(values[5].text)






navegador.close()

data_df = pd.DataFrame(datos)
data_df.to_csv("Datasets/data_olimpiadas.csv")

#print(datos)
time.sleep(5)