from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

@app.route("/test-G41/<string:cedula>",methods=['GET'])
def testMethoGet(cedula):
    variableRespuesta = {
        "respuesta": "TestGET",
        "cedula":cedula
    }
    return variableRespuesta

@app.route("/test-G41",methods=['POST'])
def testMethoPost():
    variableRespuesta = {
        "respuesta": "TestPOST"
    }
    return variableRespuesta

@app.route("/test-G41",methods=['PUT'])
def testMethoPut():
    variableRespuesta = {
        "respuesta": "TestPUT"
    }
    return variableRespuesta

@app.route("/test-G41",methods=['DELETE'])
def testMethoDelete():
    variableRespuesta = {
        "respuesta": "TestDELETE"
    }
    return variableRespuesta

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])