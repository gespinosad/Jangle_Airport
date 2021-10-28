from app import db
import pymysql


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


def comprarTickets(tickets, cc, idVuelo):
    conexion = db.obtener_conexion()
    # -ejecutar el check de los tickets si no es 0 ejecutar la compra si es 0 devolver tickets agotados y no hacer la compra
    with conexion.cursor() as cursor:
        cursor.execute("""insert into vuelosadscritos
                        select v.idVuelos,
                        v.Aviones_idAviones, %s as document, %s as tickets, v.Total * %s as Total
                        from vuelos v
                        where v.idVuelos = %s;""",
                       (cc, tickets, tickets, idVuelo))
    conexion.commit()
    conexion.close()

# Select data - using named placeholders (named style)


def comprarTickets2(tickets, cc, idVuelo):
    sql_ = """insert into vuelosadscritos
                        select v.idVuelos,
                        v.Aviones_idAviones, :cc as document, :tickets as tickets, v.Total * :tickets as Total
                        from vuelos v
                        where v.idVuelos = :idVuelo;"""
    par_ = {"cc": cc, "tickets": tickets, "idVuelo": idVuelo}
    con = db.obtener_conexion()
    with con.cursor() as cursor:
        cursor.execute(sql_, par_)
        con.commit()
        con.close()


def searchAccount(cc):
    conexion = db.obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            """
                select documentoAdministrador,Contraseña, Roles_idRoles from administrador
                where documentoAdministrador = %s
                union
                select documentoCliente,Contraseña, Roles_idRoles from cliente
                where documentoCliente = %s
                union
                select documentoPiloto,Contraseña, Roles_idRoles from piloto
                where documentoPiloto = %s""", (cc, cc, cc,))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario


def obtener_perfil_por_cccc(cc):
    conexion = db.obtener_conexion()
    perfil_user = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT Nombre, Apellido, Edad, Roles_idRoles, documentoCliente, Email FROM cliente WHERE documentoCliente = %s", (cc,))
        perfil_user = cursor.fetchone()
    conexion.close()
    return perfil_user


def agregar_usuario(documento_usuario, nombre, contraseña, roles, apellido, edad, email):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(documentoCliente, Nombre, Contraseña, Roles_idRoles, Apellido, Edad, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (documento_usuario, nombre, contraseña, roles, apellido, edad, email,))
    conexion.commit()
    conexion.close()


def obtener_perfil_piloto_por_cc(cc):
    conexion = db.obtener_conexion()
    perfil_piloto = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT Nombre, Apellido, Edad, Roles_idRoles, documentoPiloto, Email, Contraseña FROM piloto WHERE documentoPiloto = %s", (cc,))
        perfil_piloto = cursor.fetchone()
    conexion.close()
    return perfil_piloto


def obtener_vuelos_piloto():
    conexion = db.obtener_conexion()
    vuelos = []
    with conexion.cursor() as cursor:
        cursor.execute("""SELECT vuelos.Fecha, vuelos.Origen, vuelos.Destinos, aviones.idAviones, vuelos.idVuelos from vuelos inner join aviones on vuelos.Aviones_idAviones = aviones.idAviones limit 10""")
        vuelos = cursor.fetchall()
    conexion.close()
    return vuelos

    # - en el html va algo así
    #                    <td>
    #                         <form action="{{url_for('eliminar_juego')}}" method="POST">
    #                             <input type="hidden" name="id" value="{{juego[0]}}">
    #                             <button class="button is-danger">Eliminar</button>
    #                         </form>
    #                     </td>
    # - en dbConroller va algo así:
    # def eliminar_juego(id):
    # conexion = obtener_conexion()
    # with conexion.cursor() as cursor:
    #     cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
    # conexion.commit()
    # conexion.close()
    # - en allviews va algo así:
#     @app.route("/eliminar_juego", methods=["POST"])
# def eliminar_juego():
#     controlador_juegos.eliminar_juego(request.form["id"])
#     return redirect("/juegos")
