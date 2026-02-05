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
