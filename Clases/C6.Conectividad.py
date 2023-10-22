from mysql.connector import connect, Error

try:
    connection = connect(host="localhost", user="root", password="1290", database="olimpiadas")
    #print(connection)
    #print(type(connection))
    cursor = connection.cursor()
    sql = "INSERT INTO GENERO (nombre) VALUES(%s)"
    val = [("Femenino", ), ("Masculino", )]
    #EJECUTA UNA SOLA VEZ
    #cursor.execute(sql, val)
    #EJECUTA VARIAS VECES
    cursor.executemany(sql, val)
    connection.commit()
    #print(cursor.lastrowid)

    """
    sql = "show databases"
    cursor.execute(sql)
    lista = cursor.fetchall()
    for item in lista:
        print(item)
    """
except Error as e:
    print(e)