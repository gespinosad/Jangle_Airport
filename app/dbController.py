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

def obtener_perfil_por_cccc(cc):
    conexion = db.obtener_conexion()
    perfil_user = None
    with conexion.cursor() as cursor:
        cursor.execute(
           "SELECT Nombre, Apellido, Edad, Roles_idRoles, documentoCliente, Email FROM cliente WHERE documentoCliente = %s", (cc,))
        perfil_user = cursor.fetchone()
    conexion.close()
    return perfil_user




    #- en el html va algo así
    #                    <td>
    #                         <form action="{{url_for('eliminar_juego')}}" method="POST">
    #                             <input type="hidden" name="id" value="{{juego[0]}}">
    #                             <button class="button is-danger">Eliminar</button>
    #                         </form>
    #                     </td>
    #- en dbConroller va algo así: 
    # def eliminar_juego(id):
    # conexion = obtener_conexion()
    # with conexion.cursor() as cursor:
    #     cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
    # conexion.commit()
    # conexion.close()
    #- en allviews va algo así:
#     @app.route("/eliminar_juego", methods=["POST"])
# def eliminar_juego():
#     controlador_juegos.eliminar_juego(request.form["id"])
#     return redirect("/juegos")
