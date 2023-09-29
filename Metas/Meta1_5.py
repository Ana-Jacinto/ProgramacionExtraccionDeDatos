import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Nombre: Ana Beatriz Jacinto Cano     #Grupo: 951     #Ejercicio 2
# Instrucciones: Escribir una función que reciba como parámetro una lista de números.
# El método debe retornar una lista de booleanos, True si el número es divisible entre 5, False si es no es divisible.
def divisibles(numeros):
    resultado = []
    for i in numeros:
        if i %5 == 0:
            resultado.append(True)
        else:
            resultado.append(False)

    return resultado

lista = [1,2,5,10, 15]
print(divisibles(lista))

# Nombre: Ana Beatriz Jacinto Cano     #Grupo: 951     #Ejercicio 3
# Escribir una función que reciba como parámetro una lista de números, y retorne una tupla.
# El primer elemento de la tupla es la cantidad de números sin repetir de la lista, el segundo elemento de la tupla es la cantidad de números repetidos.
def duplicados(numeros):
    set_lista = set(numeros)
    repe = 0
    for i in set_lista:
        if numeros.count(i) > 1:
            repe = repe + (numeros.count(i))
    sinrepe = (len(numeros)) - repe
    lista = (sinrepe, repe)
    return (lista)

numeros=[1,3,1,4,5,3,7]
print(duplicados(numeros))

# Nombre: Ana Beatriz Jacinto Cano      #Grupo: 951     #Ejercicio 5
# Automatizar el proceso de login en la pagina de https://pypi.org/account/login/. La cual contiene una caja de texto con id username para el nombre de usuario;
# una caja de texto con id password para la contraseña y el botón de acceder (loging) con la clase “button.button—primary”. Después de loguearse debe tomar una impresión de pantalla.

#CREAR OBJETO
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size = 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://pypi.org/account/login/")

#ENCONTRAR ELEMENTO PARA INGRESAR DATOS
username = navegador.find_element(By.ID, "username")
username.send_keys("usuario123")
time.sleep(2)

password = navegador.find_element(By.ID, "password")
password.send_keys("****")
time.sleep(2)

#PARA DAR CLICK EN INICIAR CUENTA
btnlogin = navegador.find_element(By.CLASS_NAME, "button.button—primary")
btnlogin.click()

#SCREENSHOT
navegador.save_screenshot("img_test.png")
time.sleep(5)


# Nombre: Ana Beatriz Jacinto Cano      #Grupo: 951     #Ejercicio 6
# Suponga que desea tener información básica de un archivo csv, realice una clase que contenga Read_CSV que reciba la ruta del archivo a leer en el constructor.
# Dicha clase debe tener dos atributos la ruta del archivo y un atributo datos que represente al DataFrame creado apartir del archivo. Debe tener los siguientes métodos:
class Archivo:
   def __init__(self, ruta_archivo):
       self.ruta = ruta_archivo
       self.datos = pd.read_csv(ruta_archivo)

# a) primeras_lineas. Tiene como parámetro la cantidad de renglones a retornar, debe retornar los primeros N renglones de los datos.
   def primeras_lineas(self, n):
       return self.datos.head(n)

# b) ultimas_lineas. Tiene como parámetro la cantidad de renglones a retornar, debe retornar las últimas N renglones de los datos.
   def ultimas_lineas(self, n):
       return self.datos.tail(n)

# c) aleatorio_líneas. Tiene como parámetro la cantidad de renglones a retornar, debe retornar N renglones de los datos seleccionados de forma aleatoria.
   def aleatorio(self, n):
       return self.datos.sample(n)

# d) Debe crear tres propiedades (@property). La primera debe retornar una lista con los nombres de las columnas,
# la segunda debe retornar una lista con los tipos de datos de las columnas y la última una tupla con las dimensiones del DataFrame.
   @property
   def nombre (self):
       return list(self.datos.columns)

   @property
   def tipo (self):
       return list(self.datos.dtypes)

   @property
   def dimension (self):
       return self.datos.shape



