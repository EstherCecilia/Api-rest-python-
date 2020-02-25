from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'name':'Rafael'},
    {'name':'Lucas'}
]


@app.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def pessoas(id):
    if request.method == 'GET' :
        try:
            respone = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Error'}
        return jsonify(response)

    elif request.method == 'PUT' :
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE' :
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido!'})


@app.route('/insert', methods=['GET', 'POST'])
def lista():
    if request.method == 'POST' :
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'Sucesso', 'mensagem': 'Registro inserido'})
    
    if request.method == 'GET' :
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
