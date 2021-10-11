from os import error
import ssl

from flask_pymongo.wrappers import MongoClient
from app import app
from datetime import datetime
from flask import render_template, request, redirect, flash
# contendra todas nuestra vistas

connection = MongoClient('localhost', 27017)
db = connection.jangle


@app.route("/")
def index():
    return render_template("public/Landing-page/login.html")


@app.route('/home')
def vuelos():
    return render_template('public/home-user.html')


@app.route('/ingreso',  methods=['POST'])
def ingreso():
    name = request.form.get('user')
    password = request.form.get('password')
    registeredUser = db.users.find_one({"name": name, 'password': password})
    if registeredUser != None:
        return redirect('home')
    else:
        return '<h1>Wrong credentials</h1>'

@app.route('/registro',  methods=['POST','GET'])
def registrar():
    try:
        if request.method == 'POST':
            name = request.form.get('floatingName')
            lastname = request.form.get('apellido')
            id = request.form.get('identi')
            age = request.form.get('edad')
            email = request.form.get('email')
            pass1 = request.form.get('clave')
            pass2 = request.form.get('claveCon')
            registeredUser = db.users.find_one({"name": name})
            if registeredUser == None:
                if pass1 == pass2:
                    db.users.insert({
                        'name': name,
                        'lastname': lastname,
                        'identification': id,
                        'age': age,
                        'email': email,
                        'password': pass1
                    })
                    return '<h1>Added a User!</h1>'
                else:
                    return '<h1>Password does not match</h1>'
            else:
                return '<h1>There is a user with this name</h1>'
        elif request.method == 'GET':
            return render_template("public/Landing-page/registro.html")
        return ''
    except error:
        return error
