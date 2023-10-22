import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

alumnos = {"nombre": ["Octavio", "Maria     ", "Jose   ", "    Selene"],
           "genero": ["IN", "F", "M", "F"],
           "escolaridad": ["Universidad", "Universidad", "Prepa", "Secundaria"]
           }

data = pd.DataFrame(alumnos)

#BORRAR LOS ESPACIOS EN BLANCO CON LA FUNCION STR.STRIP().
data["nombre"] = data.nombre.str.strip()

#TRANSFORMAR LOS NOMBRES A MAYUSCULAS Y MINUSCULAS.
data["nombre_lower"] = data.nombre.str.lower()
data["nombre_upper"] = data.nombre.str.upper()

#data["nombre"] = data.nombre.str.strip().str.upper()

#REMPLAZAR UNA O MAS LETRAS POR OTRA CON LA FUNCION STR.REPLACE()
data["nombre_replace"] = data.nombre.str.replace("a", "x").str.replace("e", "x")

#METODOS DE FILTRADO
#Filtro de imprimir aquellos nombres que empiecen con la letra "M".
start_m = data.nombre.str.startswith("M")
#print(start_m)

#Mandar el filtro para que imprima los datos que cumplen con el filtro dentro de dataframe.
#print(data[start_m])

#Filtro de imprimir aquellos nombres que terminen con "e".
end_e = data.nombre.str.endswith("e")
#print(data[end_e])

#Filtro de imprimir aquellos nombres que contienen una "o" en cualquier parte del nomnre.
contiene_o = data.nombre.str.contains("o")
#print(data[contiene_o])

#print(data)


#TRANSFORMACION DE DATOS NOMINALES
one_hot_encoder = pd.get_dummies(data.genero)
#print(one_hot_encoder)

data = data.join(one_hot_encoder)

#TRANSFORMAR DATOS ORDINALES (STR) A NUMEROS
encoder = OrdinalEncoder(categories=[["Secundaria", "Prepa", "Universidad"]])
encoder.fit(data[["escolaridad"]])
data["educacion_encoder"] = encoder.transform(data[["escolaridad"]])

print(data)