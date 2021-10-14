from app import app
from datetime import datetime
from flask import render_template, request, redirect, flash

# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired


# contendra todas nuestra vistas
# add data base
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:password123@localhost/users"
app.config["SECRET_KEY"] = "contraseña123"
# initialize the database
# db = SQLAlchemy(app)

# # create the model

# region bd codigo
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(13), nullable=False)
#     email = db.Column(db.String(13), nullable=False, unique=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

#     # Create a string
#     def __repr__(self) -> str:
#         return "<Name %r>" % self.name


# # create a form class
# class userForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])  # imput box
#     email = StringField("Email", validators=[DataRequired()])  # imput box
#     submit = SubmitField("Submit")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     name = None
#     email = None
#     form = userForm()
#     # validate form
#     if form.validate_on_submit():
#         user = Users.query.filter_by(email=form.email.data)
#         if user is None:
#             user = Users(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ""  # se limpia para la proxima vez
#         form.email.data = ""
#     return render_template("public/sign_up.html", name=name, form=form)


# def sing_up():
#     # get to get the content and post to post it into our server
#     # this code wiil execute only when the route recieve a post request
#     if request.method == "POST":
#         req = request.form
#         # here we have several alternative to store what's in the form inside variables:
#         username = req["username"]
#         email = req.get("email")
#         password = request.form["password"]
#         print(username, email, password)
#         return redirect(request.url)
#     return render_template("public/sign_up.html")
# endregion



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