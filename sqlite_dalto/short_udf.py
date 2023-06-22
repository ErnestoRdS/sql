# Imports para conexión y formato
import sqlite3
import pandas as pd

if __name__ == '__main__':
     # Función lambda sencillita para elevar un número al cuadrado
    square = lambda n : n*n

    # Conectar a la DB
    with sqlite3.connect("./sqlite_dalto/northwind.db") as conn:
        # Crear función
        conn.create_function("square", 1, square)

        # Crear cursor
        cursor = conn.cursor()
        cursor.execute('SELECT *, square(Price) as Quad FROM Products')
        results = cursor.fetchall()
        results_df = pd.DataFrame(results)
    
    print(f"Resultados: \n {results_df}")