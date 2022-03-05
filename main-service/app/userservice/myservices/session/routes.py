from flask import request, jsonify, Blueprint, current_app, url_for, make_response
from flask_marshmallow import Marshmallow
from userservice.myservices.session.models  import Session
from userservice import db, bcrypt, login_manager, app
from userservice.myservices.decorators import require_appkey, token_required
from userservice.myservices.users.models  import User

import jwt
from datetime import datetime
import werkzeug
import os
sessions = Blueprint('sessions', __name__)
# Init marshmallow

ma = Marshmallow(sessions)
# User Schema
class SessionSchema(ma.Schema):
  class Meta:
    fields = ('idSession','token', 'idUser','loggedAt')

# Init schema
session_schema = SessionSchema(strict=True)
sessions_schema = SessionSchema(many=True, strict=True)


@sessions.route('/sessions', methods=['GET'])
@require_appkey
# @token_required
def get_sessios():
 
    all_session =Session.query.all()
    result = sessions_schema.dump(all_session)
    return jsonify(result.data)

@sessions.route('/user/statConnect', methods=['GET'])
@require_appkey
# @token_required
def nbConnect():

    all_session = db.session.query(Session , User).filter(User.id  == Session.idUser).all()
  
    result = sessions_schema.dump(all_session)
    return jsonify(result.data)