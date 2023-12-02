from mysql.connector import connect, Error
import mysql.connector

# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database. Debe crear sus métodos set y get (property, setters). Debe tener los siguientes métodos:
# a)conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
# b)desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().
class MySQL:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value


    def connect(self):
        if not self._connection:
            self._connection = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            database = self._database)

            return self._connection

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None

mysql_connection = MySQL("localhost", "root", "1290", "olimpiadas")
connection = mysql_connection.connect()
if connection:
    print("Conexion exitosa.")
    #mysql_connection.disconnect()
    #print("Conexion cerrada.")
else:
    print("No se pudo establecer la conexion.")


# Nombre: Ana Beatriz Jacinto Cano     Grupo: 951     Fecha: 20 de agosto de 2023
# Problema: Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre. Debe agregar los siguientes métodos:
# a)insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# b)editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla.
# c)eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
# d)consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%”
class PaisMySQL(MySQL):
    def __int__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, nombre):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "INSERT INTO olimpiadas.pais (id, nombre) VALUES(%s, %s)"
            cursor.execute(sql, (id, nombre))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al insertar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def editar(self, nuevo_pais, id):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.pais WHERE nombre=%s;"
            cursor.execute(sql, (nuevo_pais, ))
            if cursor.fetchall():
                return "Nombre de pais ya existente."
            else:
                sql = "UPDATE olimpiadas.pais SET nombre=%s WHERE id=%s"
                cursor.execute(sql, (nuevo_pais, id))
                connection.commit()
                return "Update realizado."
        except mysql.connector.Error as error:
            print(f"Error al editar datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def eliminar(self, id):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexcion.")

        cursor = connection.cursor()

        try:
            sql = "DELETE FROM olimpiadas.pais WHERE id = %s"
            cursor.execute(sql, (id, ))
            if cursor.rowcount == 0:
                print("No se encontró un país con el ID especificado.")
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"Error al eliminar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def consultar(self, filter):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexion.")

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.pais WHERE "+filter
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Error al consultar los datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()



#INSERTAR DATOS
pais_sql = PaisMySQL("localhost", "root", "1290", "olimpiadas")
""""
if pais_sql.insertar(3, "Londres"):
    print("Insercion correcta")
else:
    print("Error al insertar el pais.")

#MODIFICAR DATOS
if pais_sql.editar("Irlanda", 2):
    print("Nombre del país editado correctamente.")
else:
    print("Error al editar el nombre del país.")
"""

"""
#ELIMINAR DATOS
if pais_sql.eliminar(3):
    print("País eliminado correctamente.")
else:
    print("Error al eliminar el país.")

#CONSULTAR DE DATOS
resultados = pais_sql.consultar("nombre = nombre")
if resultados is not None:
    for resultado in resultados:
        print(f"ID: {resultado[0]}, Nombre: {resultado[1]}")
else:
    print("Error al consultar la base de datos.")
"""



# Desarrollar una clase llamada OlimpiadaMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# a) insertar(id, year): Método para insertar datos en la Tabla Olimpiada, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# b) editar(year): Método para editar el año en la Tabla Olimpiada. Validar que el año no exista en la tabla.
# c) eliminar(id): Método para eliminar un elemento de la Tabla Olimpiada. Debe tener como parámetro la llave primaria, retorna True si logró eliminarse y False en caso contrario.
# d) consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Olimpiada. Ejemplo: “id = 1” , “year > 1990”

class OlimpiadaMySQL(MySQL):
    def __int__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, id, year):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "INSERT INTO olimpiadas.olimpiada (id, year_olimpiada) VALUES(%s, %s)"
            cursor.execute(sql, (id, year))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al insertar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()


    def editar(self, year, new_year):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.olimpiada WHERE year_olimpiada=%s"
            cursor.execute(sql, (year, ))
            if cursor.fetchall():
                return "Año ya existente."
            else:
                sql = "UPDATE olimpiadas.olimpiada SET year_olimpiada=%s WHERE year_olimpiada=%s"
                cursor.execute(sql, (new_year, year))
                connection.commit()
                return "Update realizado."
        except mysql.connector.Error as error:
            print(f"Error al editar datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def eliminar(self, id):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexcion.")

        cursor = connection.cursor()

        try:
            sql = "DELETE FROM olimpiadas.olimpiada WHERE id = %s"
            cursor.execute(sql, (id, ))
            if cursor.rowcount == 0:
                print("No se encontró un año con el ID especificado.")
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"Error al eliminar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def consultar(self, filter):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexion.")

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.olimpiada WHERE "+filter
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Error al consultar los datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

olimpiada_sql = OlimpiadaMySQL("localhost", "root", "1290", "olimpiadas")
""""
if olimpiada_sql.insertar(1, 2020):
    print("Insercion correcta")
else:
    print("Error al insertar los datos.")

#MODIFICAR DATOS
if olimpiada_sql.editar(2020, 2000):
    print("Año editado correctamente.")
else:
    print("Error al editar el año del país.")
"""

"""
#ELIMINAR DATOS
if olimpiada_sql.eliminar(1):
    print("Año eliminado correctamente.")
else:
    print("Error al eliminar el año.")

#CONSULTAR DE DATOS
resultados = olimpiada_sql.consultar("id = 1")
if resultados is not None:
    for resultado in resultados:
        print(f"ID: {resultado[0]}, Year: {resultado[1]}")
else:
    print("Error al consultar la base de datos.")
"""

# Desarrollar una clase llamada ResultadosMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre.
# Debe agregar los siguientes métodos:
# a) insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.
# b) editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.
# c) eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.
# d) consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”.

class ResultadosMySQL(MySQL):
    def __int__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            sql = "INSERT INTO olimpiadas.resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (idOlimpiada, idPais, idGenero, oro, plata, bronce))
            connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al insertar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()


    def editar(self, idOlimpiada, idPais, idGenero, oro, plata, bronce):
        connection = self.connect()
        if not connection:
            return "Conexion no exitosa."

        cursor = connection.cursor()

        try:
            if all(isinstance(valor, int) and valor % 1 == 0 for valor in (oro, plata, bronce)):
                if oro >= 0 and plata >= 0 and bronce >= 0:
                    sql = "UPDATE olimpiadas.resultados SET oro=%s, plata=%s, bronce=%s WHERE idOlimpiada=%s and idPais=%s and idGenero=%s"
                    cursor.execute(sql, (oro, plata, bronce, idOlimpiada, idPais, idGenero))
                    connection.commit()
                    return "Update realizado."
            else:
                return "Tus valores deben ser números enteros y positivos."

        except mysql.connector.Error as error:
            print(f"Error al editar datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()

    def eliminar(self, idOlimpiada, idPais, idGenero):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexcion.")

        cursor = connection.cursor()

        try:
            sql = "DELETE FROM olimpiadas.resultados WHERE idOlimpiada = %s and idPais = %s and idGenero = %s"
            cursor.execute(sql, (idOlimpiada, idPais, idGenero))
            if cursor.rowcount == 0:
                print("No se encontró el resultado especificado.")
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"Error al eliminar datos: {error}")
            connection.rollback()
            return False
        finally:
            cursor.close()
            self.disconnect()

    def consultar(self, filter):
        connection = self.connect()
        if not connection:
            print("Error al establecer la conexion.")

        cursor = connection.cursor()

        try:
            sql = "SELECT * FROM olimpiadas.resultados WHERE "+filter
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as error:
            print(f"Error al consultar los datos: {error}")
            connection.rollback()
        finally:
            cursor.close()
            self.disconnect()


resultados_sql = ResultadosMySQL("localhost", "root", "1290", "olimpiadas")
""""
if resultados_sql.insertar(2, 2, 2, 5, 1, 6):
    print("Insercion correcta")
else:
    print("Error al insertar el pais.")

#MODIFICAR DATOS
if resultados_sql.editar(1, 1, 1, 5, 6, 8):
    print("Datos editados correctamente.")
else:
    print("Error al editar los datos.")
"""

"""
#ELIMINAR DATOS
if resultados_sql.eliminar(2, 2, 2):
    print("Fila eliminada correctamente.")
else:
    print("Error al eliminar la fila.")

#CONSULTAR DE DATOS
resultados = resultados_sql.consultar("idOlimpiada = 1")
if resultados is not None:
    for resultado in resultados:
        print(f"idOlimpiada: {resultado[0]}, idPais: {resultado[1]}, idGenero: {resultado[2]}, Oro: {resultado[3]}, Plata: {resultado[4]}, Bronce: {resultado[5]}")
else:
    print("Error al consultar la base de datos.")
"""



