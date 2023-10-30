import pandas as pd

personas = {"salario": [20000, 10000, 40000, 25000, 60000],
            "edad": [20, 18, 35, 40, 45]}

data = pd.DataFrame(personas)

#CALCULO Z-CORE X=(Xi - promedio) /std
#1) Sacar el promedio y la desviacion estandar
prom_salario = data.salario.mean()
std_salario = data.salario.std()

prom_edad = data.edad.mean()
std_edad = data.edad.std()
#print(prom_salario, std_salario, prom_edad, std_edad)

#2)Sacar el Z-score
data["zscore_salario"] = (data.salario - prom_salario) / std_salario
data["zscore_edad"] = (data.edad - prom_edad) / std_edad


#MIN-MAX: X = (Xi - Xmin) / (Xmax - Xmin)
min_salario = data.salario.min()
max_salario = data.salario.max()
data["minmax_salario"] = (data.salario - min_salario) / (max_salario - min_salario)

min_edad = data.edad.min()
max_edad = data.edad.max()
data["minmax_edad"] = (data.edad - min_edad) / (max_edad - min_edad)


#ESCALADO SIMPLE: X = (Xi) / max
data["es_salario"] = data.salario / max_salario
data["es_edad"] = data.edad / max_edad

print(data)
