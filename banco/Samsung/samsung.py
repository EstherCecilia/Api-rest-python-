# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *

app = Flask(__name__)
api = Api(app)



class Sintoma(Resource):
    def get(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : sintoma.nome,
                'id' : sintoma.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome não encontrado'}
            
        return response
    def put(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sintoma.nome = dados['nome']

        sintoma.save()

        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response
    
    def delete(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        sintoma.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_sintomas(Resource):
    def get(self):
        sintoma = Sintomas.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in sintomas]
        return response
    
    def post(self):
        dados = request.json
        sintoma = Sintomas(nome=dados['nome'])
        sintoma.save()
        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response

class Lista_doencas(Resource):
    def get(self):
        doencas = Doencas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'sintoma': i.sintoma.nome} for i in doencas]
        return response
    

    def post(self):
        dados = request.json
        sintoma = Sintomas.query.filter_by(nome=dados['sintoma']).first()
        doenca = Doencas(nome=dados['nome'], sintoma=sintoma)
        doenca.save()
        response = {
            'nome' : doenca.nome,
            'sintoma': doenca.sintoma.nome,
            'id':doenca.id
        }
        return response
        

    
    

api.add_resource(Sintoma, '/sintoma/<string:nome>')
api.add_resource(Lista_sintomas, '/sintoma')
api.add_resource(Lista_doencas, '/doenca')

if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
