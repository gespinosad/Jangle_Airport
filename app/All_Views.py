from app import app
from datetime import datetime
from flask import render_template, request, redirect
# contendra todas nuestra vistas

@app.route("/")
def index():
    return render_template("public/home-user.html")