from flask import Flask, url_for, jsonify , request,json
from elasticsearch import Elasticsearch
from datetime import datetime
from app_key import require_appkey
from difflib import SequenceMatcher

es = Elasticsearch("http://192.168.43.199")

def api_mapp():
    request_body = {
	    "settings": { 
     
        "analysis": { 
              
       
      "filter": {
        "french_elision": {
          "type":         "elision",
          "articles_case": "true",
          "articles": [
              "l", "m", "t", "qu", "n", "s",
              "j", "d", "c", "jusqu", "quoiqu",
              "lorsqu", "puisqu"
            ]
        },
        "french_stop": {
          "type":       "stop",
          "stopwords":  "_french_" 
        },
        "french_keywords": {
          "type":       "keyword_marker",
          "keywords":   ["Example"] 
        },
        "french_stemmer": {
          "type":       "stemmer",
          "language":   "light_french"
        },
         "arabic_stop": {
          "type":       "stop",
          "stopwords":  "_arabic_" 
        },
        "arabic_keywords": {
          "type":       "keyword_marker",
          "keywords":   ["مثال"] 
        },
        "arabic_stemmer": {
          "type":       "stemmer",
          "language":   "arabic"
        },"english_stop": {
          "type":       "stop",
          "stopwords":  "_english_" 
        },
        "english_keywords": {
          "type":       "keyword_marker",
          "keywords":   ["example"] 
        },
        "english_stemmer": {
          "type":       "stemmer",
          "language":   "english"
        },
        "english_possessive_stemmer": {
          "type":       "stemmer",
          "language":   "possessive_english"
        }
      },
      
      
         "analyzer": {"ngram_analyzer": {"tokenizer": "standard", "filter": ["french_elision",
            "lowercase",
            "french_stop",
            "french_keywords",
            "french_stemmer", "decimal_digit",
            "arabic_stop",
            "arabic_normalization",
            "arabic_keywords",
            "arabic_stemmer","english_possessive_stemmer",
            "lowercase",
            "english_stop",
            "english_keywords",
            "english_stemmer"],"char_filter":  [ "html_strip" ]} } } },

	   "mappings": {
    "doc_v": {
        "_source": {"enabled": "true"}, 
        "properties": {"created_at": {"type": "date"},
        "description": {"type": "text","analyzer": "ngram_analyzer"}, 
        "marque": {"type": "text","analyzer": "ngram_analyzer"}, 
        "panne"  :{"type":"keyword"},
     
        }
        } 
        }
  }
   
    res = es.indices.create(index = 'reparation', body = request_body ,ignore=[400, 404])
        
    return es
def index_doc(description,marque,panne):
   
   


    body = {
            'marque': marque ,
            'panne': panne,
            'description': description ,

        }

    
    res = es.index(index="reparation", doc_type='doc_v', body=body)
    es.indices.refresh(index="reparation")
    return res
def getAllProd():
    body={
      "query": {
          "match_all": {}
          }  ,"size": 10000,
    }
    res = es.search(index="reparation", body=body ) 
    return res

def SearchByQuery(q):
    
 


    size=50
    body={
      "query": {
        "function_score": {
       "query": {
  
           
                             "bool": {
                                   

                               "should":[
                              { "match": {
                               "marque": {
                               "query": q,
                                "boost": 6
                                 }
                                 }},
                               
                                { "match": {
                               "description": {
                               "query": q,
                                "boost": 4
                                 }
                                 }},
                                 { "match": {
                               "price": {
                               "query": q,
                                "boost": 3
                                 }
                                 }},
                                
                                 { "match": {
                               "panne": {
                               "query": q,
                                "boost": 5          
                                 }
                                 }},],
               
                             
               
                              }
                                          

                }}}  ,"size": size,
                
                 
      
             }
    res = es.search(index="reparation", body=body )
    all_hits = res['hits']['hits'] 
  


    return res

def AllProduct(panne):
    



    size=2000
    body={
      "query": {
        "function_score": {
       "query": {  
           
                             "bool": {

                                "filter" : {
                                    "script" : {
                                      "script" : {
                                      "inline": "doc['panne'].value == params.param1",
                                         "lang": "painless",
                         "params" : {
                            "param1" : panne,
                            
                        }
                     }
                }
            },
                                
               
                              }
                                          

                }}}  ,"size": size,
                
                 
      
             }
    res = es.search(index="scraping", body=body )
    all_hits = res['hits']['hits'] 
  


    return res     