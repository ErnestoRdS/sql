# Import para poder trabajar con SQLite
import sqlite3
# Import para formatear lo que regresen las consultas
import pandas as pd


# Función Main
if __name__ == '__main__':
    
    # Función lambda sencillita para elevar un número al cuadrado
    square = lambda n : n*n

    # Conexión
    conn = sqlite3.connect("./sqlite_dalto/northwind.db")

    # Registrar la función en la base de datos
    '''Parámetros: nombre_para_db, #params, nombre_func_py'''
    conn.create_function("square", 1, square)

    '''
        Necesitamos algo que nos permita consultar a una base de datos
        y obtener la respuesta, pero...
        Si se hace una consulta a la DB, para poder obtener una respuesta,
        hay que recibir los datos, procesarlos, etc

        Los cursores nos permiten consultar, devolver y procesar una consulta,
        y con una función nos devuelve la información ya formateada
    '''
    # Crear un cursor
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT * FROM Products
        '''
    )

    results = cursor.fetchall()
    # Formatear
    results_df = pd.DataFrame(results)

    '''
        Al ejecutar una consulta desde otro lenguaje, automáticamente
        estamos iniciando una transacción, por lo que hay que asentar
        los cambios, o simplemente terminar la transacciónxd
    '''
    # Terminar transacción
    conn.commit()

    # Una vez obtenidos los resultados, hay que cerrar el cursor
    cursor.close()
    # Iwal la conexión
    conn.close()


    print(results_df)

