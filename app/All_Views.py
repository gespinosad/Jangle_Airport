from app import app
from datetime import datetime
from flask import render_template, request, redirect, flash


# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired


# contendra todas nuestra vistas

# Landing Page

@app.route("/")
def login():
    return render_template("public/Landing-page/login.html")


@app.route("/registro")  # esto es el link que ponemos en el menú para cambiar de pagina
def registro():
    return render_template("public/Landing-page/registro.html")

# Usuario


@app.route("/mi-perfil-usuario")
def my_profile_user():
    return render_template("/public/usuarios/Mi_Perfil_Usuario.html")


@app.route("/mis-vuelos-usuario")
def mis_vuelos_user():
    return render_template("/public/usuarios/Mis_Vuelos_Usuario.html")


@app.route("/compra-usuario")
def compra_user():
    return render_template("/public/usuarios/Usuario_compra.html")


@app.route("/home-user")
def homeUser():
    return render_template("public/home-user.html")

# Piloto


@app.route("/mi-perfil-piloto")
def piloto_mi_perfil():
    return render_template("/public/Piloto/mi-perfil.html")


@app.route("/mis-vuelos-piloto")
def piloto_mis_vuelos():
    return render_template("/public/Piloto/mis-vuelos.html")
