# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *
from random import *
from datetime import *

app = Flask(__name__)
api = Api(app)



class SintomaPorDoencas(Resource):
    def get(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        
        try:
            response = {'sintomas':[{'nome':s.nome} for s in doenca.sintomas]}

                

        except AttributeError:
            response = {'status': False}
            
        return response



class Sintoma(Resource):
    def get(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : sintoma.nome,
                'id' : sintoma.id

                }

        except AttributeError:
            response = {'status': False}
            
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
        response = [{'id':i.id, 'nome':i.nome} for i in sintoma]
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




class TransmicaoPorDoencas(Resource):
    def get(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        
        try:
            response = {'transmicao':[{'nome':s.nome} for s in doenca.transmicao]}

                

        except AttributeError:
            response = {'status': False}
            
        return response





class Transmicao(Resource):
    def get(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : transmicao.nome,
                'id' : transmicao.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    def put(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            transmicao.nome = dados['nome']
            transmicao.save()

        response = {
            'id' : transmicao.id,
            'nome' : transmicao.nome
            }

        return response
    
    def delete(self, nome):
        transmicao = Transmicaos.query.filter_by(nome=nome).first()
        transmicao.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_transmicaos(Resource):
    def get(self):
        transmicao = Transmicaos.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in transmicao]
        return response
    
    def post(self):
        dados = request.json
        transmicao = Transmicaos(nome=dados['nome'])
        transmicao.save()
        response = {
            'id' : transmicao.id,
            'nome' : transmicao.nome
            }

        return response




class PrevencaoPorDoencas(Resource):
    def get(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        print(doenca.nome)
        
        try:
            response = {'prevencoes':[{'nome':p.nome} for p in doenca.prevencao]}

                

        except AttributeError:
            response = {'status': False}
            
        return response



class Prevencao(Resource):
    def get(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : prevencao.nome,
                'id' : prevencao.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    def put(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            prevencao.nome = dados['nome']
            prevencao.save()

        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response
    
    def delete(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        prevencao.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_prevencoes(Resource):
    def get(self):
        prevencao = Prevencoes.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in prevencao]
        return response
    
    def post(self):
        dados = request.json
        prevencao = Prevencoes(nome=dados['nome'])
        prevencao.save()
        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response

class Sala(Resource):
    def get(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        try:
            response = {
                'status': True,
                'nome' : sala.nome,
                'senha' : sala.senha,
                'id' : sala.id

                }

        except AttributeError:
            response = {'status': False}
            
        return response
    
    def put(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sala.nome = dados['nome']
            
        if 'senha' in dados:
            sala.senha = dados['senha']

        sala.save()

        response = {
                'nome' : sala.nome,
                'senha' : sala.senha,
                'id' : sala.id

                }

        return response
    
    def delete(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        sala.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class SetStart(Resource):
    def get(self, id):
        sala = Salas.query.filter_by(id=id).first()
        try:
            sala.partida = True
            sala.save()
            response = {'status':True}
        except AttributeError:
            response = {'status':False}
        return response

class GetStart(Resource):
    def get(self, id):
        sala = Salas.query.filter_by(id=id).first()
        try:
            response = {'status':sala.partida}
        except AttributeError:
            response = {'status':False}
        return response
    

class Lista_salas(Resource):
    def get(self):
        sala = Salas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'senha':i.senha} for i in sala]
        return response
    
    def post(self):
        dados = request.json
        salaCheck = Salas.query.filter_by(nome=dados['nome']).first()
        
        try:
            salaCheck.nome = dados['nome']
            response = {
                'status':False
                

            }

        except AttributeError:
            sala = Salas(nome=dados['nome'], senha=dados['senha'], partida=False)
            sala.save()
            response = {
                    'status':True,
                    'nome' : sala.nome,
                    'senha' : sala.senha,
                    'id' : sala.id

                }

        return response



class Doenca(Resource):
    def get(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : doenca.nome,
                'tipo' : doenca.tipo,
                'agente' : doenca.agente,
                'id' : doenca.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome n�o encontrado'}
            
        return response
    
    def put(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            doenca.nome = dados['nome']
            doenca.save()

        if 'tipo' in dados:
            doenca.nome = dados['tipo']
            doenca.save()

        if 'agente' in dados:
            doenca.nome = dados['agente']
            doenca.save()

        
        response = {
                'nome' : doenca.nome,
                'tipo' : doenca.tipo,
                'agente' : doenca.agente,
                'id' : doenca.id

                }

        return response
    
    def delete(self, nome):
        doenca = Doencas.query.filter_by(nome=nome).first()
        doenca.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}



class Lista_doencas(Resource):
    def get(self):
        doencas = Doencas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'tipo':i.tipo, 'agente':i.agente, 'sintomas':[{'nome':s.nome} for s in i.sintomas], 'transmicao':[{'nome':s.nome} for s in i.transmicao], 'prevencao':[{'nome':s.nome} for s in i.prevencao]} for i in doencas]
        
        return response
    

    def post(self):
        dados = request.json
        prevencao = Prevencoes.query.filter_by(nome=dados['prevencao']).first()
        doenca = Doencas(nome=dados['nome'], agente=dados['agente'], tipo=dados['tipo'])
        doenca.save()
        return "Doen�a inserida com sucesso!"
        
class Lista_sessao(Resource):
    def get(self, id):

        sessao = Sessao.query.filter_by(id_sessao=id).first()
        doenca = Doencas.query.all()

        try:
            responDoenca = [{'nome':i.nome} for i in doenca]
        except AttributeError:
            responDoenca = []

        
        try:
            dica = Dicas.query.filter_by(id_sessao=id).first()
            reponseDica = {'sintomas':[{'nome':s.nome} for s in dica.sintoma], 'transmicao':[{'nome':s.nome} for s in dica.transmicao], 'prevencao':[{'nome':s.nome} for s in dica.prevencao]}
        except AttributeError:
            reponseDica = []
        
        try:
            try:
                tamanho = len(sessao.doencas)
                doenc = sessao.doencas[tamanho-1].nome
            except IndexError:
                doenc = ""
                
            responseSessao = {'id_sessao': sessao.id_sessao, 'rodada':sessao.rodada}
            response = {'status':True, 'sessao':responseSessao,'dicas':reponseDica, 'ultimaDoenca': doenc,'doencasSelecionadas':[{'nome':d.nome} for d in sessao.doencas], 'doencas':responDoenca}
                          
  
        except AttributeError:
            response = {'status':False}

            
        return response


class Lista_sessoes(Resource):
    def post(self):
        dados = request.json

        sala = Salas.query.filter_by(nome=dados['nome']).first()
        doenca = Doencas.query.all()

        responDoenca = [{'nome':i.nome} for i in doenca]


        
        sessao = Sessao.query.filter_by(id_sessao=sala.id).first()
        
        
        try:
            response = {'status':False, 'id_sessao':sessao.id_sessao,'sala':sala.nome, 'doencas':responDoenca}
                 
        except AttributeError:
            
            if sala.senha == dados['senha']:
                sessaoNova = Sessao(id_sessao=sala.id, rodada=0,  doencas=[])
                sessaoNova.save()
                dica = Dicas(id_sessao=sessaoNova.id_sessao, sintoma=[], prevencao=[], transmicao=[])
                dica.save()
                print(dica.id)
                response = {'status':True, 'id_sessao':sessaoNova.id_sessao,'sala':sala.nome, 'doencas':responDoenca}
            else:
                response = {'status':False}   

            
        return response

    def put(self):
        dados = request.json
        sessao = Sessao.query.filter_by(id_sessao=dados['id_sessao']).first()
        doenca = Doencas.query.filter_by(nome=dados['doenca']).first()
        dica = Dicas.query.filter_by(id_sessao=dados['id_sessao']).first()

        print(sessao.rodada)
        
        if dados['rodada'] != sessao.rodada:
            print(dica.id)
            dics = db_session.query(conectedSintomaSessaos).filter(conectedSintomaSessaos.c.id_sessao == dica.id)
            dics.delete(synchronize_session=False)
            db_session.commit()
            
            dics2 = db_session.query(conectedTransmicaoSessaos).filter(conectedTransmicaoSessaos.c.id_sessao == dica.id)
            dics2.delete(synchronize_session=False)
            db_session.commit()
            
            dics3 = db_session.query(conectedPrevencaoSessaos).filter(conectedPrevencaoSessaos.c.id_sessao == dica.id)
            dics3.delete(synchronize_session=False)
            db_session.commit()
            
            
                           
        if 'dicas' in dados:
            if 'sintoma' in dados['dicas']:
                sintoma = Sintomas.query.filter_by(nome=dados['dicas']['sintoma']).first()
                try:
                    print(sintoma.nome)
                    dica.sintoma.append(sintoma)
                    dica.save()
                except AttributeError:
                    print("Error")
            if 'prevencao' in dados['dicas']:
                prevencao = Prevencoes.query.filter_by(nome=dados['dicas']['prevencao']).first()
                try:
                    dica.prevencao.append(prevencao)
                    dica.save()
                except AttributeError:
                    print("Error")

            if 'transmicao' in dados['dicas']:
                transmicao = Transmicaos.query.filter_by(nome=dados['dicas']['transmicao']).first()
                try:
                    dica.transmicao.append(transmicao)
                    dica.save()
                except AttributeError:
                    print("Error")

            
        try:
            sessao.rodada = dados['rodada']
            sessao.save()
            
            sessao.doencas.append(doenca)
            sessao.save()
            
            try:
                sintomas = [{'nome':s.nome} for s in dica.sintoma]
                transmissoes = [{'nome':s.nome} for s in dica.transmicao]
                prevencoes = [{'nome':s.nome} for s in dica.prevencao]
                reponseDica = {'sintomas':sintomas, 'transmicao': transmissoes, 'prevencao': prevencoes}
            except AttributeError:
                reponseDica = []

            try:
                
                reponseSelecionadas = [{'nome':d.nome} for d in sessao.doencas]
            except AttributeError:
                reponseSelecionadas = []

            tamanho = len(sessao.doencas)
            doenc = sessao.doencas[tamanho-1].nome
            response = {'status':True, 'id_sessao':sessao.id_sessao,'dicas':reponseDica, 'ultimaDoenca': doenc, 'rodada':sessao.rodada,'doencasSelecionadas':reponseSelecionadas}


        except AttributeError:
            response = {
                'status':False

            }

        return response


class Listar_Ranking(Resource):
    def get(self, id):
        try:
            jogador = Ranking.query.filter_by(id_sessao=id).all()
            jogador_ordenado = sorted(jogador, key = Ranking.get_pontuacao, reverse=True)
            try:
                responseAdivinhador = [{'nome':i.nome, 'pontuacao':i.pontuacao} for i in jogador_ordenado]
            except AttributeError:
                responseAdivinhador = [{'nome':"Saiu", 'pontuacao':0}]

            jogadorDica = Ranking.query.filter_by(id_sessao=id).filter_by(adivinhador=False).first()
            try:
                responseDicas = {'nome':jogadorDica.nome}
            except AttributeError:
                responseDicas = {'nome':"Saiu"}
            response = {'status': True, 'darDica':responseDicas, 'jogadores':responseAdivinhador}

        except AttributeError:
            response = {'status': False}
            
        
        return response




        
class Jogador(Resource):
    def get(self, nome, id):
        jogador = Ranking.query.filter_by(nome=nome).filter_by(id_sessao=id).first()
        try:
            response = {
                'nome' : jogador.nome,
                'id_sesao' : jogador.id_sessao,
                'pontuacao' : jogador.pontuacao,
                'id' : jogador.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome n�o encontrado'}
            
        return response
    

    def delete(self, nome):
        jogador = Ranking.query.filter_by(nome=nome).first()
        jogador.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}



class Lista_jogadores(Resource):
    def get(self):
        dados = request.json
        jogador = Ranking.query.filter_by(id_sessao=dados['id_sessao']).all()
        
        jogador_ordenado = sorted(jogador, key = Ranking.get_pontuacao, reverse=True)
        

        responseAdivinhador = [{'nome':i.nome, 'pontuacao':i.pontuacao} for i in jogador_ordenado]

        jogadorDica = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=False).first()

        try:
            responseDicas = {'nome':jogadorDica.nome}
        except AttributeError:
            responseDicas = {'nome':""}
            
        response = {'darDica':responseDicas, 'jogadores':responseAdivinhador}
        return response

    def put(self):
        dados = request.json
        pontuac = Ranking.query.filter_by(nome=dados['nome']).filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=True).first()
        adivinhador =Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(adivinhador=False).first()


        
        try:
            rodada = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(rodada=dados['rodada']).all())
            pontuac.rodada = dados['rodada']
            pontuac.ordem = rodada + 1
            ponti = (1/(pontuac.ordem))*10
            
            if dados['fim'] == True :
                ponti = 0
            else:
                ponti = (1/(pontuac.ordem))*10


            ponto = pontuac.pontuacao + ponti
            pontuac.pontuacao = ponto
            pontuac.save()


            adivinhador.pontuacao = adivinhador.pontuacao + ponti*0.75
            adivinhador.save()
            adivinhador.rodada = dados['rodada']
            adivinhador.save()

            response = {
                'status':True,
                'nome' : pontuac.nome,
                'id_sessao' : pontuac.id_sessao,
                'ordem': pontuac.ordem,
                'id' : pontuac.id,
                'pontuacao': pontuac.pontuacao
                

            }

            

        except AttributeError:
            response = {
                'status':False

            }

        x = len(Ranking.query.filter_by(rodada=dados['rodada']).filter_by(id_sessao=dados['id_sessao']).all())
        y = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).all()) 
        if y == x:
            adivinhador.adivinhador = True
            adivinhador.save()
            adivinhador.ordem = 300
            adivinhador.save()

            aux = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter(Ranking.ordem!=300).all()
            try:
                aux[0].adivinhador = False
                aux[0].save()
            except IndexError:
                print("Error")

        
        

        return response


        
    def post(self):
        dados = request.json
        pontuac = Ranking.query.filter_by(id_sessao=dados['id_sessao']).filter_by(nome=dados['nome']).first()

        sala = Salas.query.filter_by(id=dados['id_sessao']).first()
        

        if sala.partida:
            response = {
                'status':False,
                'mensagem':"Sessao j� foi iniciada"    
            }
        else:
            try:
                pontuac.nome = dados['nome']
                response = {
                'status':False,
                'mensagem':"Esse nome ja existe"
                

                }

            except AttributeError:
                ponto = 0
                rodada = 0
                ordem = len(Ranking.query.filter_by(id_sessao=dados['id_sessao']).all()) + 1
                if ordem == 1 :
                    adivinhador = False
                else:
                    adivinhador = True
                jogador = Ranking(nome=dados['nome'],  rodada = rodada, id_sessao=dados['id_sessao'], pontuacao=ponto, ordem=ordem, adivinhador=adivinhador)
                jogador.save()

                response = {
                    'status':True,
                    'nome' : jogador.nome,
                    'id_sessao' : jogador.id_sessao,
                    'id' : jogador.id,
                    'pontuacao': jogador.pontuacao,
                    'adivinhador': jogador.adivinhador
                

                }

        
        

        return response



class Encerra_jogadores(Resource):
    def delete(self):
        dados = request.json
        jogador = Ranking.query.filter_by(nome=dados['nome']).filter_by(id_sessao=dados['id_sessao']).first()

        try:
            jogador.delete()
            response = {'status': True}

            
            sessao = Sessao.query.filter_by(id_sessao=dados['id_sessao']).all()
            sala = Salas.query.filter_by(id=dados['id_sessao']).first()
            
            try:
                sessao.delete()
                sala.partida = False
                sala.save()

            except AttributeError:
                print("J� foi excluido")
            


        except AttributeError:
            response = {'status': False}

        return response




class Home(Resource):
    def get(self):
        return "Bem vindo, Adiciona um endpoint para melhor navegar na api"

class Time(Resource):
    def get(self):
        #time.sleep(300)
        return {'status':True, 'time':0}


    

api.add_resource(Home, '/')
api.add_resource(Time, '/time')
api.add_resource(SetStart, '/setComecou/<int:id>')
api.add_resource(GetStart, '/getComecou/<int:id>')

api.add_resource(Listar_Ranking, '/ranking/<int:id>')
api.add_resource(Jogador, '/jogador/<string:nome>/<int:id>')
api.add_resource(Lista_jogadores, '/jogador')
api.add_resource(Encerra_jogadores, '/jogador/encerra')

api.add_resource(Sintoma, '/sintoma/<string:nome>')
api.add_resource(Lista_sintomas, '/sintoma')
api.add_resource(SintomaPorDoencas, '/sintomas/<string:nome>')

api.add_resource(Transmicao, '/transmicao/<string:nome>')
api.add_resource(Lista_transmicaos, '/transmicao')
api.add_resource(TransmicaoPorDoencas, '/transmicaos/<string:nome>')

api.add_resource(Prevencao, '/prevencao/<string:nome>')
api.add_resource(Lista_prevencoes, '/prevencao')
api.add_resource(PrevencaoPorDoencas, '/prevencaos/<string:nome>')

api.add_resource(Sala, '/sala/<string:nome>')
api.add_resource(Lista_salas, '/sala')

api.add_resource(Doenca, '/doenca/<string:nome>')
api.add_resource(Lista_doencas, '/doenca')

api.add_resource(Lista_sessao, '/sessao/<int:id>')
api.add_resource(Lista_sessoes, '/sessao')

if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
