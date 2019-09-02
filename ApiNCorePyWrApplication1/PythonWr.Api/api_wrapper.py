
###------------------------------------------------------------------
###Python API wrapper
###Designed by AnaSoft Inc. 2019
###
###Get template extension with Postman and Python unit tests
###http://www.anasoft.net/apipython
### 
###------------------------------------------------------------------

import flask
from flask import request, jsonify, session, redirect, url_for
import json
import requests
from config import Config
from flasgger import Swagger
from flasgger import swag_from

app = flask.Flask(__name__)
app.config["DEBUG"] = True
Swagger(app)

#base service url
api_url_base = Config.API_URL_BASE


###------------------------------------------------------------------
###Base API
###------------------------------------------------------------------

###
###Flasgger Swagger specification token and account example
###https://github.com/rochacbruno/flasgger
###
###http://localhost:5000/apidocs/
###

###----------------------------------
@app.route('/', methods=['GET'])
def home():
    return "<h1>Python API wrapper by Anasoft Inc.</h1><p>This is Python API wrapper for API service PythonWr.Api</p><a class='btn btn-outline-primary' role='button' href='/api/info'><b>Base API specification with Swagger</b></a><br><a class='btn btn-outline-primary' role='button' href='http://localhost:5000/apidocs/'><b>Swagger Python API specification</b></a>"

###----------------------------------
#/api/info
@app.route('/api/info', methods=['GET'])
def api_info():
    try:
        api_url = '{0}/api/info'.format(api_url_base)
        resp = requests.get(api_url)
        return resp.text
    except Exception as e:
        return str(e)

###----------------------------------
#/api/token
@app.route('/api/token', methods=['POST'])
def api_token():
    """
    file: flasgger/apitoken.yml
    """
    try:
        loginInfo = json.loads(request.get_data())  #get passed credentials
        api_url = '{0}api/token'.format(api_url_base)
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(api_url, json=loginInfo)
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=200,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###------------------------------------------------------------------
###Account API
###------------------------------------------------------------------

#Add account
@app.route('/api/account', methods=['POST'])
def api_account_add()
    """
    file: flasgger/api_account_add.yml
    """
    try:
        data = json.loads(request.get_data())  
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/account'.format(api_url_base)
        resp = requests.post(api_url, json=data, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=201,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#GetAll accounts
@app.route('/api/account', methods=['GET'])
def api_account_get_all():
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/account'.format(api_url_base)
        resp = requests.get(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=200,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#GetById account
@app.route('/api/account/<id>', methods=['GET'])
def api_account_get_one(id):
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/account/{1}'.format(api_url_base,id)
        resp = requests.get(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=200,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#UpdateById account
@app.route('/api/account/<id>', methods=['PUT'])
def api_account_update_one(id):
    try:
        data = json.loads(request.get_data())  
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/account/{1}'.format(api_url_base,id)
        resp = requests.put(api_url, json=data, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=202,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#DeleteById account
@app.route('/api/account/<id>', methods=['DELETE'])
def api_account_delete_one(id):
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/account/{1}'.format(api_url_base,id)
        resp = requests.delete(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=None,
            status=204,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###------------------------------------------------------------------
###User API
###------------------------------------------------------------------

#Add user
@app.route('/api/user', methods=['POST'])
def api_user_add():
    try:
        data = json.loads(request.get_data())  
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/user'.format(api_url_base)
        resp = requests.post(api_url, json=data, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=201,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#GetAll users
@app.route('/api/user', methods=['GET'])
def api_user_get_all():
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/user'.format(api_url_base)
        resp = requests.get(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=200,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#GetById user
@app.route('/api/user/<id>', methods=['GET'])
def api_user_get_one(id):
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/user/{1}'.format(api_url_base,id)
        resp = requests.get(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=200,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#UpdateById user
@app.route('/api/user/<id>', methods=['PUT'])
def api_user_update_one(id):
    try:
        data = json.loads(request.get_data())  
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/user/{1}'.format(api_url_base,id)
        resp = requests.put(api_url, json=data, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=json.dumps(resp.json()),
            status=202,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)

###----------------------------------
#DeleteById user
@app.route('/api/user/<id>', methods=['DELETE'])
def api_user_delete_one(id):
    try:
        headers=setAuthenticationHeader(request.headers)
        api_url = '{0}api/user/{1}'.format(api_url_base,id)
        resp = requests.delete(api_url, headers=headers)
        #check response error
        respError = checkRespError(resp,api_url)
        if respError is not None:
            return respError
        #if all good return json 
        response = app.response_class(
            response=None,
            status=204,
            mimetype='application/json; charset=utf-8')
        return response
    except Exception as e:
         return str(e)


###------------------------------------------------------------------
###Common functions
###------------------------------------------------------------------
def checkRespError(response,api_url):
  if response.status_code >= 500:
      return '[!] [{0}] Server ErrorZ'.format(response.status_code) 
     # return None
  elif response.status_code == 404:
      return('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
  elif response.status_code == 401:
      return('[!] [{0}] Authentication Failed'.format(response.status_code))
  elif response.status_code >= 400:
      return('[!] [{0}] Bad Request'.format(response.status_code))
      #print(response.content )
  elif response.status_code >= 300:
      return('[!] [{0}] Unexpected redirect.'.format(response.status_code))
  else:
      return None

###----------------------------------
def setAuthenticationHeader(headers):
    auth = headers.get("Authorization")
    if auth is None:
        return('[!] Authentication Failed')
    access_token= str(auth).replace('Bearer ','')
    return {'Content-Type':'application/json',
             'Authorization': 'Bearer {}'.format(access_token)}

###----------------------------------
if __name__ == '__main__':
    app.run(debug=True)
