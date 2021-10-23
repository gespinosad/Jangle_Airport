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


def get_vuelo_por_doc_user(cc):
    conexion = db.obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT vuelos.idVuelos, aviones.idAviones, cliente.documentoCliente, cliente.Nombre, 
vuelos.Origen, vuelos.Destinos, vuelos.Fecha, vuelos.Tickets 
from vuelos inner join aviones on vuelos.Aviones_idAviones = aviones.idAviones 
inner join vuelosadscritos on vuelosadscritos.vuelos_idVuelos = vuelos.idVuelos 
inner join cliente on cliente.documentoCliente = vuelosadscritos.cliente_documentoCliente 
where cliente.documentoCliente = %s""", (cc,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

# -falta


def actualizar_juego(tickets, piloto):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                       (tickets, piloto))
    conexion.commit()
    conexion.close()


def buscar_usuario_por_doc(cc):  # para buscar en login si el usuario existe en la db
    conexion = db.obtener_conexion()
    user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT documentoCliente, Contraseña FROM cliente where documentoCliente= %s", (cc,))
        user = cursor.fetchone()
    conexion.close()
    return user
