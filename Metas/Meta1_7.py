import pandas as pd


alumnos = {"Nombre": ["Octavio", "Maria", "Jose", None, "Selene", None, "Diego", "Diego", "Octavio", None],
           "Genero": ["Masculino", "Femenino", "Masculino", None, "Masculino", "Femenino", None, "Masculino", "Masculino", "Masculino"],
           "Escolaridad": ["Universidad",None, "Universidad", "Preparatoria", "Secundaria", None, "Preparatoria", None, "Universidad", "Secundaria"]
           }

dataframe = pd.DataFrame(alumnos)


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.
def nulos(data):
    return data.isnull().sum() / len(data.isnull())

data = dataframe
#print(nulos(data))


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
def duplicados(data):
    return data.duplicated().sum()

data = dataframe
#print(f"Numero de renglones duplicados: {duplicados(data)}")


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje.
# Este debe eliminar todas las columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original.
# Retornar la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1.

def eliminar_nulos(data, porcentaje):
    if 0 <= porcentaje <= 1:
        entero = round(len(data) * porcentaje)
        nuevo_data = data.dropna(axis="columns", thresh=entero)
        eliminados = list(set(data.columns) - set(nuevo_data.columns))
        return f"Lista de columna(s) eliminada(s) porque no cuentan con el mínimo de {porcentaje}% de valores NO nulos: {eliminados}"
    else:
        return "El porcentaje debe estar entre 0 y 1."

data = dataframe
porcentaje = 0.80
#print(eliminar_nulos(data, porcentaje))


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena.
# La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción.
# Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
def sustitucion(data, list, cadena):
    if cadena not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'.")

    if cadena == "mean":
        if pd.api.types.is_numeric_dtype(data[list]):
            new_data = data[list].mean()
        else:
            raise ValueError(f"La columna '{list}' no es numérica, por lo que no se puede usar 'mean'.")
    elif cadena == "bfill":
        new_data = data[list].bfill()
    else:
        new_data = data[list].ffill()

    return new_data

data = dataframe
list = ["Nombre", "Genero", "Escolaridad"]
cadena = "ffill"

#print(sustitucion(data, list, cadena))


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original.
# Debe retornar la cantidad de renglones eliminados.
def repetidos(data):
    drop_duplicates = data.drop_duplicates()
    eliminados = len(data) - len(drop_duplicates)
    return f"La cantidad de renglones eliminados es: {eliminados}"

data = dataframe

#print(repetidos(data))

