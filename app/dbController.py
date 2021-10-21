from app import db


def obtener_vuelos():
    conexion = db.obtener_conexion()
    vuelos = []
    with conexion.cursor() as cursor:
        cursor.execute("""select vuelos.idVuelos, vuelos.Origen, vuelos.Destinos, vuelos.Fecha,
        vuelos.HoraSalida from vuelos limit 10""")
        vuelos = cursor.fetchall()
    conexion.close()
    return vuelos


def obtener_vuelo_por_id(id):
    conexion = db.obtener_conexion()
    vuelo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select idVuelos, Origen, Destinos, Fecha, HoraSalida, Aviones_idAviones, Tickets, Total from vuelos where idVuelos = %s", (id,))
        vuelo = cursor.fetchone()
    conexion.close()
    return vuelo


def obtener_usuario_por_key(id, cc):
    conexion = db.obtener_conexion()
    vuelo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            """select documentoCliente, Nombre, Tickets, Total
                from cliente, vuelos where idVuelos=%s and documentoCliente=%s;""", (id, cc))
        vuelo = cursor.fetchone()
    conexion.close()
    return vuelo

# -falta


def actualizar_juego(tickets, piloto):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                       (tickets, piloto))
    conexion.commit()
    conexion.close()


def buscar_usuario_por_id():
    conexion = db.obtener_conexion()
    user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "select idVuelos, Origen, Destinos, Fecha, HoraSalida, Aviones_idAviones, Tickets, Total from vuelos where idVuelos = %s", (id,))
        user = cursor.fetchone()
    conexion.close()
    return user
