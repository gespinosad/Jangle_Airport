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


def hacer_Compra(tickets, cc):
    conexion = db.obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""insert into vuelosadscritos
                        select v.idVuelos,
                        v.Aviones_idAviones, %s as document, %s as tickets, v.Total * %s as Total
                        from vuelos v
                        where v.idVuelos = 555;""",
                       (cc, tickets, tickets))
    conexion.commit()
    conexion.close()

# Select data - using named placeholders (named style)


def hacer_compra2(tickets, cc, idVuelo):
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


def query_named(point_id="", analyte="", sampling_date=""):
    sql_ = "SELECT * FROM gw_assay WHERE point_id = :id AND analyte = :a AND sampling_date = :d"
    par_ = {"id": point_id, "a": analyte, "d": sampling_date}

    cnn = sqlite3.connect("groundwater.db")
    cur = cnn.cursor()
    cur.execute(sql_, par_)
    records = cur.fetchall()
    cnn.close()
    return records


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
