# database.py
import pyodbc

def conectar_bd():
    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=10.1.100.65;'  # Cambia esto por tu servidor
            'DATABASE=CicloE;'  # Cambia esto por tu base de datos
            'UID=serviciosdesarrollo;'  # Cambia esto por tu usuario
            'PWD=D3v3saD3v!'  # Cambia esto por tu contraseña
        )
        return conexion
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# Función de prueba para verificar la conexión
def probar_conexion():
    conexion = conectar_bd()
    if conexion:
        print("Conexión exitosa a la base de datos.")
        conexion.close()  # Siempre cierra la conexión cuando termines
    else:
        print("Fallo en la conexión a la base de datos.")

# Ejecutar la función de prueba si se corre el archivo directamente
if __name__ == "__main__":
    probar_conexion()