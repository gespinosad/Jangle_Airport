from db import obtener_conexion


def obtener_cuentas():
    conexion = obtener_conexion()
    cuentas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido, rol, FROM Cuentas")
        cuentas = cursor.fetchall()
    conexion.close()
    return cuentas
