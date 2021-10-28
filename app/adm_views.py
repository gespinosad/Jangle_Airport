from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app
from flask import render_template, session
# contendra todas nuestra vistas


@app.route("/admin/admin_cuentas")
def admin_adm_cuentas():
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-cuentas.html")
    return redirect(url_for("logout"))


@app.route("/admin/admin_vuelos")
def admin_adm_vuelos():
    if session["account"] == 1:
        return render_template("/public/Administrador/Admin-vuelos.html")


@app.route("/admin/agregar_cuentas")
def admin_agg_cuentas():
    if session["account"] == 1:
        return render_template("/public/Administrador/Agregar-cuentas.html")


@app.route("/admin/agregar_vuelos")
def admin_agg_vuelos():
    if session["account"] == 1:
        return render_template("/public/Administrador/Agregar-vuelos.html")
