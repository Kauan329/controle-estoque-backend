from flask import Flask, request, jsonify
from datetime import datetime
import os
import json

app = Flask(__name__)

@app.route("/estoque", methods=["POST"])
def receber_dados():
    dados = request.json
    print(f"Dados recebidos: {dados}")
    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
