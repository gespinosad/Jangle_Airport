from app import app
from flask import render_template
# contendra todas nuestra vistas


@app.route("/admin/admin_cuentas")
def admin_adm_cuentas():
    return render_template("/public/Administrador/Admin-cuentas.html")

@app.route("/admin/admin_vuelos")
def admin_adm_vuelos():
    return render_template("/public/Administrador/Admin-vuelos.html")

@app.route("/admin/agregar_cuentas")
def admin_agg_cuentas():
     return render_template("/public/Administrador/Agregar-cuentas.html")

@app.route("/admin/agregar_vuelos")
def admin_agg_vuelos():
     return render_template("/public/Administrador/Agregar-vuelos.html")