#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Dada una lista de números enteros, retorna True si al menos un valor aparece dos veces, y Falso si todos los elementos son distintos.
def Duplicados(numeros):
    numeros_set = set(numeros)
    return len(numeros_set) != len(numeros)

numeros1 = [1,2,3,2,4]
print(Duplicados(numeros1))


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Dado una lista de números enteros y un valor entero (target), retorna el índice de los dos números que sumados sean igual al target.
#Debe asumir que existe siempre una única solución, y que los elementos no se pueden usar dos veces. Debes retornar una tupla con los índices.
def BusquedaSuma(nums, target):
    dic = {}
    for i in nums:
        if i in dic:
            print(dic[i], nums.index(i))
        faltante = target - i
        dic[faltante] = nums.index(i)

nums = [2, 3, 7, 15, 11]
target = 9
print(BusquedaSuma(nums,target))


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Diseñe una función encripta(s, clave), que reciba un string s con un mensaje y un string con una clave de codificación, y retorne el mensaje codificado según la clave leída.
#Los signos de puntuación y dígitos que aparecen en el mensaje deben conservarse sin cambios. La clave consiste en una sucesión de las 26 letras minúsculas del alfabeto, las cuales se hacen corresponder con el alfabeto básico (a...z, sin la ñ o vocales acentuadas) de 26 letras.
#La primera letra de la clave se relaciona con la letra 'a', la segunda con la letra 'b', etc.
def Ecriptar(list_mensaje, list_clave):
    encriptado = ''
    for i in list_mensaje:
        if i in list_abcedario:
            indice = list_abcedario.index(i)
            letra = list_clave[indice]
            encriptado = encriptado + letra
        else:
            encriptado = encriptado + i
    print(encriptado)

list_abcedario = list('abcdefghijklmnopqrstuvwxyz')
list_clave = list('ixmrklstnuzbowfaqejdcpvhyg')
list_mensaje = list('cafe')

print(Ecriptar(list_mensaje, list_clave))


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Diseña una función desencripta(s, clave) que realice la función inversa a la función anterior,
#es decir, reciba un string s y una clave y realice la desencriptación del mensaje en el string devolviendo la cadena desencriptada.
def Desencriptado(encriptado, abecedario):
    desencriptado = ''
    for i in encriptado:
        if i in clave:
            indice = clave.index(i)
            palabra = abecedario[indice]
            desencriptado = desencriptado + palabra
        else:
            desencriptado = desencriptado + i
    print(desencriptado)


abecedario = list('abcdefghijklmnopqrstuvwxyz')
clave = list('ixmrklstnuzbowfaqejdcpvhyg')
encriptado = list('riok 1 mtfmfbidk')

print(Desencriptado(encriptado, abecedario))


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo una lista o diccionario de objetos de tipo Pensionista (Elija a conveniencia si una lista o diccionario).
#Cada objeto de Pensionista tiene los siguientes atributos: identificador del pensionista (string), un entero que indica la edad y una serie de gastos mensuales que se guardan (lista de enteros).
#La clase GrupoPensionistas debe tener los siguientes métodos:
class GrupoPensionista:
    def __init__(self, identificador, nombre, edad, gastos):
        self.Identificador = identificador
        self.Nombre = nombre
        self.Edad = edad
        self.Gastos = gastos

    def media_gastos(self):
        prom = sum(self.Gastos)/len(self.Gastos)
        return prom

    def promedio_edades(self, pensionistas):
        edades = [p.Edad for p in pensionistas]
        prom = sum(edades)/len(edades)
        print("La media de edad es de ", prom)

    def edades_extremas(self, pensionistas):
        edades = [p.Edad for p in pensionistas]
        menor = min(edades)
        mayor = max(edades)
        print("La edad mas chica es de ", menor, "Y la edad mas grande es de ", mayor)

    def gastos_pensionados(self, pensionistas_gastos):
        prom = sum(pensionistas_gastos)/len(pensionistas_gastos)
        print("El promedio de gastos de todos los pensionistas es de ", prom)

    def media_maxima(self, pensionistas):
        mayor_promedio = max(pensionistas, key=lambda x: x.media_gastos())
        return f"El pensionista con el mayor gasto promedio es {mayor_promedio.Nombre} (ID: {mayor_promedio.Identificador}) con un gasto promedio de ${mayor_promedio.media_gastos():.2f}"

    def gastos_prom(self,pensionistas):
        pensionistas_ordenados = sorted(pensionistas, key=lambda x: x.media_gastos(), reverse=True)
        result = "Gasto promedio de cada pensionista (de mayor a menor):\n"
        for pensionista in pensionistas_ordenados:
            result += f"{pensionista.Nombre}: ${pensionista.media_gastos():.2f}\n"
        return result

pensionista1 = GrupoPensionista(110,"Carlos",80,(587,908,243))
pensionista2 = GrupoPensionista(111, "Andrea",95, (120,1543,399))
pensionista3 = GrupoPensionista(112,"Nathan",72, (1890,2653,744))

pensionistas = [pensionista1, pensionista2, pensionista3]

# a)Dado el identificador o índice de un pensionista, devuelva el promedio de los gastos.
print("El promedio de gastos del pensionista ", pensionista1.Identificador, "es de:", pensionista1.media_gastos())
print("El promedio de gastos del pensionista ", pensionista2.Identificador, "es de:", pensionista2.media_gastos())
print("El promedio de gastos del pensionista ", pensionista3.Identificador, "es de:", pensionista3.media_gastos())

# b)Dado todos los pensionados, devuelve el promedio de las edades.
print(pensionista1.promedio_edades(pensionistas))

# c)Dado todos los pensionados, devuelva al pensionado con menor y mayor edad en una tupla.
print(pensionista1.edades_extremas(pensionistas))

# d)Dado todos los pensionados, devuelva la suma del promedio de los gastos de todos los pensionistas de la lista.
pensionistas_gastos = pensionista1.Gastos + pensionista2.Gastos + pensionista3.Gastos
print(pensionista1.gastos_pensionados(pensionistas_gastos))

# e)Dado todos los pensionistas, retorne el mayor promedio de los gastos entre todos los pensionistas de la lista, su nombre e identificador.
print(pensionista1.media_maxima(pensionistas))

# f)gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el gasto promedio de cada persona. La lista resultante debe estar ordenada de forma ascendente.
print(pensionista1.gastos_prom(pensionistas))


#Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
#Problema: Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual puede contener repetidos. Debe contener los siguientes métodos:
class Estadistica():
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuencia(self):
        dicc = {}
        for i in self.numeros:
            if i in dicc:
                dicc[i] += 1
            else:
                dicc[i] = 1
        return dicc

    def moda(self):
        frecuencias = self.frecuencia()
        mode = max(frecuencias, key=frecuencias.get)
        return mode

    def histograma(self):
        frecuencias = self.frecuencia()
        for i, frecuencia in sorted(frecuencias.items()):
            print(f'{i}: {"*" * frecuencia}')


numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
estadistica = Estadistica(numeros)


# a)Dada la lista devuelve un diccionario con el número de veces que aparece cada número en la lista.
print("Diccionario de Frecuencia: ",estadistica.frecuencia())

# b)Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
print("La moda es: ",estadistica.moda())

# c)Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.
print("Histograma:")
estadistica.histograma()
