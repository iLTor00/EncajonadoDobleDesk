# logic.py
from database import conectar_bd

def ejecutar_encajonado_lectura_primarias(codbar, nCaja, nUsuarioID, ingresarPrimaria, controlHomogeneo):
    conexion = conectar_bd()
    if not conexion:
        return None  # No se puede conectar

    cursor = conexion.cursor()

    try:
        # Ejecutar el SP con parámetros
        cursor.execute("""
            EXEC [dbo].[Encajonado_Lectura_Primarias_Cortes] 
            @codbar=?, 
            @nCaja=?, 
            @nUsuarioID=?, 
            @ingresarPrimaria=?, 
            @controlHomogeneo=?
        """, (codbar, nCaja, nUsuarioID, ingresarPrimaria, controlHomogeneo))
        
        # Obtener los resultados
        resultados = cursor.fetchall()
        
        conexion.close()
        return resultados
    except Exception as e:
        print(f"Error ejecutando SP Encajonado_Lectura_Primarias_Cortes: {e}")
        conexion.close()
        return None
