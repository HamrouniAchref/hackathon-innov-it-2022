from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, types
from datetime import datetime
from userservice import db
from flask import current_app
from flask_login import UserMixin



# Registred User Class/Model

class Reparation(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=False, nullable=False)
    password= db.Column(db.String(60), nullable=False)
    solde = db.Column(db.String(60), nullable=False)
    quantite=db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(150), nullable = False)
    role = db.Column(db.String(150), nullable = False)
    city = db.Column(db.String(150), nullable = False)

 


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')


    # Init constructorlevelConfidence_user,
    def __init__(self, firstname, lastname, email, phone_number, password, role,status,quantite,solde,city):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.role = role
        self.isLogged = False
        self.status = False
        self.city = city
        self.status = status
        self.quantite = quantite
        self.solde = solde
