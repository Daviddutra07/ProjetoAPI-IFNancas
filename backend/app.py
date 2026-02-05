from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = "items.json"

TIPOS_PERMITIDOS = ["entrada", "saida"]
STATUS_PERMITIDOS = ["ativo", "concluido", "arquivado"]

# Funções para o JSON

def carregar_items():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_items(items):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def buscar_item(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None

def validar_item(dados):
    if "titulo" not in dados or len(dados["titulo"].strip()) < 3:
        return "Titulo é obrigatório e deve ter no mínimo 3 caracteres"

    if "tipo" not in dados or dados["tipo"] not in TIPOS_PERMITIDOS:
        return "Tipo inválido"

    if "status" not in dados or dados["status"] not in STATUS_PERMITIDOS:
        return "Status inválido"

    if "valor" in dados and dados["valor"] < 0:
        return "Valor não pode ser negativo"

    return None

# Rotas

@app.route("/items", methods=["GET"])
def listar_items():
    items = carregar_items()

    tipo = request.args.get("tipo")
    status = request.args.get("status")

    if tipo:
        itens_filtrados = []
        for item in items:
            if item["tipo"] == tipo:
                itens_filtrados.append(item)
        items = itens_filtrados

    if status:
        itens_filtrados = []
        for item in items:
            if item["status"] == status:
                itens_filtrados.append(item)
        items = itens_filtrados


    return jsonify(items), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def obter_item(item_id):
    items = carregar_items()
    item = buscar_item(items, item_id)

    if item is None:
        return jsonify({"error": "Item não encontrado"}), 404

    return jsonify(item), 200