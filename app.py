from flask import Flask
from flask import request

import json

app = Flask(__name__)
'''
IMPLEMENTAR DUAS FUNÇÕES DE ROTA 
para um App de comida.
1- Listar todos os pratos (GET)
2- Adicionar um novo prato (GET)
'''
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/lista_pratos", methods=['GET'])
def lista_pratos():
    arq = open("payload.json", "r")
    data = arq.read()
    return json.dumps(data)

@app.route("/add_prato",methods=['POST'])
def add_prato():
    arq = open("payload.json")
    data = arq.read()
    data = json.loads(data)
    novo_item = {
      "id": 10,
      "produto": "Coxinha",
      "categoria": "Lanche",
      "preco": 350.0
    }
    data['cardapio'].append(novo_item)
    arq = open("payload.json", "w")
    arq.write(json.dumps(data))
    return {"msg": "Item adicionado com sucesso!"
            , "item": novo_item,
            "status": 200
            }