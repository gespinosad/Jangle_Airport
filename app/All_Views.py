from app import app
from datetime import datetime
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# contendra todas nuestra vistas
# add data base
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://users.db"
app.config["SECRET_KEY"] = "contraseña123"
# initialize the database
db = SQLAlchemy(app)

# create the model


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(13), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a string
    def __repr__(self) -> str:
        return "<Name %r>" % self.name


# create a form class
# def userForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])  # imput box
#     submit = SubmitField("Submit")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     name = None
#     form = userForm()
#     # validate form
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ""  # se limpia para la proxima vez
#     return render_template("sing_up.html", name=name, form=form)
def sing_up():
    # get to get the content and post to post it into our server
    # this code wiil execute only when the route recieve a post request
    if request.method == "POST":
        req = request.form
        # here we have several alternative to store what's in the form inside variables:
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        print(username, email, password)
        return redirect(request.url)
    return render_template("public/sign_up.html")


@app.route("/")
def index():
    return render_template("public/home-user.html")
