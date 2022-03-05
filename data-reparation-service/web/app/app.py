from flask import Flask, url_for, jsonify , request,json
from elasticsearch import Elasticsearch
from datetime import datetime
from app_key import require_appkey
from difflib import SequenceMatcher
from indexation_elasticsearch import Indexation


import os


import sys
if sys.version_info.major < 3:
    reload(sys)

es = Elasticsearch("http://192.168.43.199:9200")
#es = Elasticsearch("http://elasticsearch:9200")
#es = Elasticsearch("http://localhost:9200")


app = Flask(__name__)

@app.before_first_request
def api_mapp():
  Indexation.api_mapp()

   





@app.route('/info')
@require_appkey
def api_info():
   return jsonify(es.info())



@app.route('/')
def api_root():
    return 'Welcome to the reparation API'


@app.route('/addSmartphone')  
def addSmartphone():
  try:
    marque= request.json['marque']
    description= request.json['description']
    panne= request.json['panne']
  except:
    return jsonify({"msg":"erreur insertion "})  
  return Indexation.index_doc(description,marque,panne) 
    


@app.route('/getAllSmartphones')
@require_appkey
def getAllSmartphones():
  try:
    return Indexation.getAllProd()
  except:
    return jsonify({"msg":"erreur"})  
   


@app.route('/search')
@require_appkey
def search():
  try:

    q= request.json['q']
  except:
    return jsonify({"msg":"requete q introuvalble "})  
  return Indexation.SearchByQuery(q) 


@app.route('/searchByPanne')
@require_appkey
def searchByPanne(): 
    try:

      panne= request.json['panne']
    except:
      return jsonify({"msg":" introuvalble "})

    return Indexation.AllProduct(panne)





@app.route('/getAllProd')
@require_appkey
def getAllProd():
  
    return Indexation.getAllProd()


 
      


@app.route('/mapp')
@require_appkey
def api_mapp():
  
  e=Indexation.api_mapp()
   
  return e.indices.get_alias("*")  


@app.route('/deleteIndex')
@require_appkey
def deleteIndex():
    

    res =es.indices.delete(index='reparation', ignore=[400, 404])
    Indexation.api_mapp()
    return es.indices.get_alias("*") 

  
@app.route('/testInd')
def dtett():
    

    
    return jsonify(es.indices.get_alias("*"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5050')