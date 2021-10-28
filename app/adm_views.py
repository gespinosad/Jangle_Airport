from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app, dbController
from flask import render_template, session, request
# contendra todas nuestra vistas


@app.route("/admin/admin_cuentas")
def admin_adm_cuentas():
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-cuentas.html")
    return redirect(url_for("logout"))


@app.route("/admin/admin_vuelos")
def admin_adm_vuelos():
    print("Entre al route")
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-vuelos.html")


@app.route("/admin/agregar_cuentas", methods=["POST", "GET"])
def admin_agg_cuentas():
    if session["account"] == 1:
      if request.method == "POST":
            nombre = request.form.get("nombre")
            apellido = request.form.get("apellido")
            documento_usuario = request.form.get("documento_usuario")
            edad = request.form.get("edad")
            email = request.form.get("email")
            clave = request.form.get("contraseña")
            roles = 2
            dbController.agregar_usuario(documento_usuario, nombre, clave, roles, apellido, edad, email)
    misCuentas = dbController.obtener_cuentas()
    return render_template("/public/Administrador/Agregar-cuentas.html", misCuentas=misCuentas)


@app.route("/admin/agregar_vuelos")
def admin_agg_vuelos():
    if session["account"] == 1:
        return render_template("/public/Administrador/Agregar-vuelos.html")
