
#IMPORTACIONES
#REQUEST: Retorna un codigo y el htp de la pagina.
import requests
#BS4: Retorna partes de un html.
from bs4 import BeautifulSoup
import pandas as pd

#GET = Traeme una paguina web (la parte de desarrollo de la paguina)
response = requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
#print(response.content)

#CODIGO 200: La paguina esta bien.
#CODIGO 400: Errores de la paguina. Por ejemplo l 404 Significa que una paguina no existe.
#COGIDO 500: Errores del servidor.

#Parser = Dscomponer en pedacitos las etiquetas de la paguina.
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.head.title.text)
    lista_divs = soup.find_all("div", attrs={"class": "card-content"})

    data = {"Puesto": [], "Empresa": [], "Ciudad": [], "Fecha": []}

    for i in lista_divs:
        puesto = i.find("h2", attrs={"class": "title is-5"})
        company = i.find("h3", attrs={"class": "subtitle is-6 company"})
        city = i.find("p", attrs={"class": "location"})
        date = i.find("time")

        data["Puesto"].append(puesto.text)
        data["Empresa"].append(company.text)
        data["Ciudad"].append(city.text.strip())
        data["Fecha"].append(date.text)

    data_df = pd.DataFrame(data)
    data_df.to_csv("Datasets/jobs.csv")

"""
        print(puesto.text)
        print(company.text)
        #STRIP: Elimina los espacios es blanco.
        print(city.text.strip())
        print(date.text)
        print("\n")
    #print(lista_divs[0].prettify()) 

else:
    print(f"Error {response.status_code} al momento de cargar la pagina") """