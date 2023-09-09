import pandas as pd

jobs = pd.read_csv("Datasets/jobs.csv", index_col=0)

print(jobs.describe())
#Encontrar los puestos con esa descripcion de trabajo.
print(jobs[jobs.Puesto == "Python Programmer (Entry-Level)"])