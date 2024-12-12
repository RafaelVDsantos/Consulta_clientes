from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask("Minha API")
CORS(app)

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/consulta", methods=["GET"])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    if registro["nome"] == "Não encontrado":
        return jsonify({"erro": "Cliente não encontrado"}), 404
    return jsonify(registro)

@app.route("/cadastre", methods=["POST"])
def cadastrar():
    payload = request.json
    cpf = payload.get("cpf")
    valores = payload.get("dados")

    dados_existentes = carregar_arquivo()
    if cpf in dados_existentes:
        return jsonify({"erro": "CPF já cadastrado"}), 400

    salvar_dados(cpf, valores)
    return jsonify({"mensagem": "Dados cadastrados com sucesso!"}), 201
    
def carregar_arquivo():
    caminho_arquivo = "data/clientes.json"
    try: 
        with open(caminho_arquivo, "r") as arq:
            return json.load(arq)
    except Exception:
        return {}

def gravar_arquivo(dados):
    caminho_arquivo = "data/clientes.json"
    try: 
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
        return "Dados armazenados" 
    except Exception:
        return "Falha ao gravar o arquivo"

def salvar_dados(cpf, registro):
    dados_pessoas = carregar_arquivo()
    dados_pessoas[cpf] = registro
    dados_pessoas_ordenados = {
        k: v for k, v in sorted(dados_pessoas.items(), key=lambda item: item[1].get("nome", "").lower())
    }
    gravar_arquivo(dados_pessoas_ordenados)

def dados(cpf):
    dados_pessoas = carregar_arquivo()
    return dados_pessoas.get(cpf, {"nome": "Não encontrado", "data_nascimento": "Não encontrado", "email": "Não encontrado"})

if __name__=="__main__":
    app.run(debug=True)
 