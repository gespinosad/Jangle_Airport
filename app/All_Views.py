from app import app
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, session, url_for
from app import dbController
from passlib.hash import pbkdf2_sha256
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

# https://www.youtube.com/watch?v=xbedZg38dy4
# https://www.youtube.com/watch?v=L0b_0KhkuBk
# contendra todas nuestra vistas
# Landing Page


@app.route("/")
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["CC"]
        getUser = dbController.buscar_usuario_por_doc(user)
        contraseña = request.form["contraseña"]
        # comparar la contraseña asi:
        #! if pbkdf2_sha256.verify(contraseña, getUser[1])
        if getUser != None:
            if user == str(getUser[0]) and contraseña == str(getUser[1]):
                session["usuario"] = user
                # Aquí puedes colocar más datos. Por ejemplo
                # session["nivel"] = "administrador"
                return redirect(url_for("homeUser"))
        #! raise ValidationError("Usuario o contraseña incorrectos")
    return render_template("public/Landing-page/login.html")


@app.route("/registro")  # esto es el link que ponemos en el menú para cambiar de pagina
def registro():

    #! hashed_pswd = pbkdf2_sha256.hash(contraseña)  hashear contraseña
    return render_template("public/Landing-page/registro.html")

# Cerrar sesión


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


@app.before_request
def antes_de_cada_peticion():
    ruta = request.path
    print("imprimiendo ruta: ", ruta)
    # Si no ha iniciado sesión y no quiere ir a algo relacionado al login, lo redireccionamos al login
    if not 'usuario' in session and ruta != "/login" and ruta != "/registro" and not ruta.startswith("/static"):
        return redirect("/login")
        # flash("Inicia sesión para continuar")
    # Si ya ha iniciado, no hacemos nada, es decir lo dejamos pasar
# Usuario


@app.route("/mi-perfil-usuario")
def my_profile_user():
    perfil_user = dbController.obtener_perfil_por_cccc(session["usuario"])
    return render_template("/public/usuarios/Mi_Perfil_Usuario.html", perfil_user=perfil_user)


@app.route("/mis-vuelos-usuario")
def mis_vuelos_user():
    miVuelo = dbController.get_vuelo_por_doc_user(session["usuario"])
    return render_template("/public/usuarios/Mis_Vuelos_Usuario.html", miVuelo=miVuelo)


@app.route("/compra-usuario/<int:id>")
def compra_user(id):
    vuelo = dbController.obtener_vuelo_por_id(id)
    return render_template("/public/usuarios/Usuario_compra.html", vuelo=vuelo)


@app.route('/compra-usuario', methods=["POST"])
def hacerCompra():
    cc = session["usuario"]
    tickets = request.form["nTickets"]
    idVuelo = request.form["id"]
    print(id)
    dbController.comprarTickets(tickets, cc, idVuelo)
    return redirect("/home-user")


@app.route("/home-user")
def homeUser():
    vuelos = dbController.obtener_vuelos()
    return render_template("public/home-user.html", vuelos=vuelos)

# Piloto


@app.route("/mi-perfil-piloto")
def piloto_mi_perfil():
    return render_template("/public/Piloto/mi-perfil.html")


@app.route("/mis-vuelos-piloto")
def piloto_mis_vuelos():
    return render_template("/public/Piloto/mis-vuelos.html")
