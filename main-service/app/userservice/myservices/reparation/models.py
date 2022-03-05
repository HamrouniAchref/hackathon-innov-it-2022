from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, types
from datetime import datetime
from userservice import db
from werkzeug import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin



# Registred User Class/Model

class Reparation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200), nullable=False)
   



    # Init constructorlevelConfidence_user,
    def __init__(self, desc):
        self.desc = desc
      
