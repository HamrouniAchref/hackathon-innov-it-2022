from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, types
from datetime import datetime
from userservice import db
from werkzeug import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin



# Registred User Class/Model

class Session(UserMixin, db.Model):
    idSession = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256))
    idUser =  db.Column(db.Integer )
    loggedAt = db.Column(db.String(256))

    # Init constructorlevelConfidence_user,
    def __init__(self,token , idUser , loggedAt  ):
        self.token = token
        self.idUser = idUser
        self.loggedAt = loggedAt
        
