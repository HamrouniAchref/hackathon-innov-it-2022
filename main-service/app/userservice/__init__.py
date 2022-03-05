from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Locate the DB file

basedir = os.path.abspath(os.path.dirname(__file__))


# Init app

app = Flask(__name__)

# Init db

db = SQLAlchemy(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Init mail
mail = Mail(app)


# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:@Mysql/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', 'flask'),
    os.getenv('DB_PASSWORD', ''),
    os.getenv('DB_HOST', 'mysql'),
    os.getenv('DB_NAME', 'flask')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
RESERVE_CONTEXT_ON_EXCEPTION = False
app.config['SECRET_KEY'] = "thisismysecretkey!"
app.config['FLASKY_GROUPS_PER_PAGE'] =  3
app.config['FLASKY_FOLLOWERS_PER_PAGE'] = 3
MAIL_SERVER = 'smtp.googlemail.com'
login_manager = LoginManager(app)
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# Init marshmallow
ma = Marshmallow(app)
from userservice.myservices.users.routes import users
from userservice.myservices.mylistes.routes import mylistes
from userservice.myservices.compte.routes import comptes
from userservice.myservices.operation.routes import operations
from userservice.myservices.invitation.routes import invitations
from userservice.myservices.commenter.routes import commenters
from userservice.myservices.session.routes import sessions
from userservice.myservices.classe.routes import classes
from userservice.myservices.section.routes import sections
from userservice.myservices.matiere.routes import matieres
from userservice.myservices.chapitre.routes import chapitres
from userservice.myservices.settings.routes import settings


app.register_blueprint(users)
app.register_blueprint(mylistes)
app.register_blueprint(comptes)
app.register_blueprint(operations)
app.register_blueprint(invitations)
app.register_blueprint(commenters)
app.register_blueprint(sessions)
app.register_blueprint(classes)
app.register_blueprint(sections)
app.register_blueprint(matieres)
app.register_blueprint(chapitres)
app.register_blueprint(settings)

   #app.register_blueprint(userservice.api.routes.mod, url_prefix='/api')

