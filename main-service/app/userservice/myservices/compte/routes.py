from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
from userservice.myservices.users.models import User
from userservice.myservices.compte.models import Compte
from userservice import db
from userservice.myservices.decorators import token_required, require_appkey
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from userservice.myservices.operation import routes

# Init bluebripnt
comptes= Blueprint('comptes', __name__)

# Init marshmallow
ma = Marshmallow(comptes)

# Compte Schema
class CompteSchema(ma.Schema):
  class Meta:
    fields = ('numc','email','typeCompte' ,  )

# Init schema
compte_schema = CompteSchema(strict=True)
comptes_schema = CompteSchema(many=True, strict=True)


# Join a Group
#@comptes.route('/newcompte', methods=['POST'])
#@require_appkey
#@token_required
def new_compte(email,typeCompte):
    #if not current_user:
    #    return jsonify ({ 'msg': 'Cannot perform that function, token is missing!' })
 
    
    #if not Compte.query.filter_by (email=email  ).first() :
        now=datetime.now()
        datecreation = now.strftime("%m/%d/%Y %H:%M:%S")
        new_compte = Compte( email ,0 ,datecreation,typeCompte,0,0 ) 
        db.session.add (new_compte)
        db.session.commit ()
         
        return 'New compte successfully added !'
                         
                          

   # return  'User already in the Compte !' 
                    

# Delete compte 
@comptes.route('/deletecompte', methods=['DELETE'])
@require_appkey
@token_required
def delete_compte(current_user):
    if not current_user:
        return jsonify({'msg': 'Cannot perform that function, token is missing!'})

    numc = request.json['numc']
    comptedel = Compte.query.filter_by(numc=numc).first()

    if not comptedel :
        return jsonify({'msg': 'No Compte found!'})

    db.session.delete(comptedel)
    db.session.commit()

    return jsonify({'msg': 'compte successfully deleted!'})  

@comptes.route('/compte/getcompte', methods=['GET'])
@require_appkey
@token_required
def get_compte(current_user):
    typeCompte = request.json['typeCompte']

    if not current_user:
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
    email = current_user.email
    compte = Compte.query.filter_by (email=email,typeCompte=typeCompte ).first() 
    if not compte :
        return jsonify({'msg': 'No Compte found!'})

    return compte_schema.jsonify(compte)

@comptes.route('/compte/updatenbrVue', methods=['PUT'])
@require_appkey
@token_required
def updatenbrVue(current_user):
    if not current_user:
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
    email = request.json['email']
    nbrVue = request.json['nbVue']
    compte = Compte.query.filter_by (email=email  ).first() 
    if not compte :
        return jsonify({'msg': 'No Compte found!'})                 
    compte.nbrVuePayes  = nbrVue 
    db.session.commit()
    return compte_schema.jsonify(compte)


@comptes.route('/compte/updatenbrDocument', methods=['PUT'])
@require_appkey
@token_required
def updatenbrDocument(current_user):
    if not current_user:
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
    email = request.json['email']
    nbDoc = request.json['nbDocument']
    compte = Compte.query.filter_by (email=email  ).first() 
    if not compte :
        return jsonify({'msg': 'No Compte found!'})                 
    compte.nbrDocumentPayes  = nbDoc 
    db.session.commit()
    return compte_schema.jsonify(compte)


@comptes.route('/compte/addpoint', methods=['PUT'])
@require_appkey
@token_required
def addPoint(current_user):
    if not current_user:
        return jsonify ({ 'message': 'Cannot perform that function, token is missing!' })
    email = request.json['email']
    montant = request.json['montant']
    compte = Compte.query.filter_by (email=email  ).first() 
    if not compte :
        return jsonify({'msg': 'No Compte found!'})                 
    compte.point  = compte.point + montant 
    db.session.commit()
    return compte_schema.jsonify(compte)