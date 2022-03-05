from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/test')
def getStuff():
    return '{"result" : "welcome inferno"}'

