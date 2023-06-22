# Imports para conexión y formato
import sqlite3
import pandas as pd

# Import para las gráficas
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Conectarnos
    conn = sqlite3.connect("./sqlite_dalto/northwind.db")

    '''
        SE TRABAJARÁN 2 CONSULTAS:
        1) EL PRODUCTO MÁS RENTABLE
        2) EL EMPLEADO CON MÁS VENTAS
    '''
    # Para consultar el producto más rentable
    query1 = '''
        SELECT
            p.ProductName,
            SUM(Price * Quantity) AS Revenue
        FROM OrderDetails od
        JOIN Products p ON od.ProductID = p.ProductID
        GROUP BY od.ProductID
        ORDER BY Revenue DESC
        LIMIT 10
    '''
    # A la función read_sql_query(consulta, conexión)
    top_products = pd.read_sql_query(query1, conn) 
    # Graficar productos top
    top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5), legend=False)

    plt.title("Top Products")
    plt.xlabel("Productos")
    plt.ylabel("Utilidadesxd")
    plt.xticks(rotation=90)
    plt.show()

    # Para consultar el empleado con más ventas
    query2 = '''
        SELECT
            FirstName || " " || LastName AS Employee,
            COUNT(*) as Ventas
        FROM Orders o
        JOIN Employees e ON o.EmployeeID = e.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY Ventas DESC
    '''
    top_employees = pd.read_sql_query(query2, conn)
    top_employees.plot(x="Employee", y="Ventas", kind="bar", figsize=(10,5), legend=False)

    plt.title("Top Employees")
    plt.xlabel("Empleados")
    plt.ylabel("Ventas")
    plt.xticks(rotation=45)
    plt.show()
