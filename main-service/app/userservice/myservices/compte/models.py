from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, types
from datetime import datetime
from userservice import db
from werkzeug import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin




class Compte(UserMixin,db.Model):
    numc = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    


    # Init constructor
    def __init__(self, email ,typeCompte ):
        self.email = email
       
        self.typeCompte = typeCompte 
