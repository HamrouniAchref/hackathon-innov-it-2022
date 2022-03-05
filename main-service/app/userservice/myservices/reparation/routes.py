from flask import request, jsonify, Blueprint, current_app, url_for, make_response
from flask_marshmallow import Marshmallow
from userservice import db, bcrypt, login_manager, app
from userservice.myservices.decorators import require_appkey, token_required
from userservice.myservices.compte import routes
from userservice.myservices.session.models import Session

import jwt
from datetime import datetime
import os
users = Blueprint('users', __name__)
# Init marshmallow


