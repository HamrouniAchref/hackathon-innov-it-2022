from flask import request, jsonify, Blueprint, current_app, url_for, make_response
from flask_marshmallow import Marshmallow
from userservice.myservices.users.models  import User
from userservice import db, bcrypt, login_manager, app
from userservice.myservices.decorators import require_appkey, token_required
from userservice.myservices.compte import routes
from userservice.myservices.session.models import Session

import jwt
from datetime import datetime
import os
users = Blueprint('users', __name__)
# Init marshmallow
@app.before_first_request
def create_tables():
    db.create_all()
ma = Marshmallow(users)
# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id','firstname', 'lastname', 'email', 'phone_number', 'quantite', 'password', 'city', 'role','solde','status')

# Init schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

def getuser (email): 
    return  User.query.filter_by(email=email).first()




@users.route('/user/signup', methods=['POST'])
@require_appkey
def create_account():
    email = request.json['email']
    # Fetch user
    user = getuser(email)
    if user is None:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email= request.json['email']
        phone_number = request.json['phone_number']
        password = request.json['password']
        password = bcrypt.generate_password_hash (request.json['password']).decode ('utf-8')
        role = request.json['role']
        status = request.json['status']
        quantite = request.json['quantite']
        solde = request.json['solde']

        city = request.json['city']
            

     
        new_user = User(firstname, lastname, email, phone_number, password, role,status,quantite,solde,city)
        db.session.add(new_user)
        db.session.commit()
       
        routes.new_compte(email,role)
       


        return jsonify ({'msg': 'New account successfully created !' })
    else:
         return jsonify({ 'msg': 'Email address is already registred !' })


@users.route('/users', methods=['GET'])
@require_appkey
@token_required
def get_users(current_user):
    if not current_user :
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
   
    all_users =User.query.filter_by(isDeleted= 0).all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)




@users.route('/user/<string:email>', methods=['GET'])
@require_appkey
@token_required
def get_user_mail(current_user,email):
    if not current_user:
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
   
    
    user = getuser(email)
    
    if not user:
      return jsonify({ 'msg': 'No user found!'
                       })
    return user_schema.jsonify(user)





@users.route("/user/login", methods=['GET', 'POST'])
@require_appkey
def login():
    auth = request.authorization
    email = request.json['email']
    pwd = request.json['password']
    user = getuser(email)

    if not user or user.isDeleted == True :

        return jsonify({ 'isLogged': False,
                         'msg': "Une adresse courriel est invalide"})


    if bcrypt.check_password_hash(user.password, pwd) :
        token = jwt.encode (
            { 'id': user.id },
            current_app.config['SECRET_KEY'])
        user.isLogged =True
        token = token.decode('UTF-8')
        d=datetime.now()
        loggedAt = d.strftime("%m/%d/%Y, %H:%M:%S")
        new_session = Session(token, user.id , loggedAt)
        db.session.add(new_session)
        db.session.commit()
        return jsonify ({ 'token': token ,
                          'idUser': user.id,
                          'firstname': user.firstname,
                          'lastname': user.lastname,
                          'email': user.email,
                          'phone_number': user.phone_number,
                          'city': user.city,
                          'role': user.role,
                          'msg': 'User successfully logged in !'
                          })

    user.isLogged = False
    return jsonify ({
        
        'msg': 'Mot de passe incorrect. Réessayez ou cliquez sur "Mot de passe oublié" pour le réinitialiser.'
    })


# Logout
@users.route("/user/logout", methods=['GET', 'POST'])
@require_appkey
@token_required
def logout(current_user):
    if not current_user:
        return jsonify ({ 'msg': 'Cannot perform that function, token is missing!' })
    
    token = request.headers['x-access-token']
    user = getuser(current_user.email)
    if user is None:
        user.isLogged = True
        return jsonify ({
        'isLogged': user.isLogged,
        'msg': 'Failed to log out !'
    })
    else:
        current_session = Session.query.filter_by(token=token).first()
        db.session.delete(current_session)
        db.session.commit()
        return jsonify ({
                'isLogged': user.isLogged,
                'msg': 'User successfully logged out !'
            })

