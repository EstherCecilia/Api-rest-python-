# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'name':'Rafael', 'id':0},
    {'name':'Lucas', 'id':1}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Error', 'mensagem':'Id não encontrado'}
        except Exception:
            response = {'status': 'Error', 'mensagem': 'Erro desconhecido'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Lista_Desenvolvedores, '/dev')

if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
