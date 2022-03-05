from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc, types
from datetime import datetime
from userservice import db




# Registred User Class/Model

class Recyclage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(200), nullable=False)
   



    # Init constructorlevelConfidence_user,
    def __init__(self, desc):
        self.desc = desc
      
