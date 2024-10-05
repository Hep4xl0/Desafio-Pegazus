from flask import Blueprint, request, jsonify
from src.helpers.helper import salvar_contas, contas
from src.models.banco_model import cadastro

# Cria um Blueprint para as rotas
app = Blueprint('app', __name__)

@app.route('/contas', methods=['GET'])
def visualizar_contas():
    return jsonify([{'nome': conta.nome, 'cpf': conta.cpf, 'saldo': conta.saldo} for conta in contas])

@app.route('/contas/criar', methods=['POST'])
def criar_conta():
    data = request.json
    nome = data.get('nome')
    cpf = data.get('cpf')

    if not cpf.isdigit() or len(cpf) != 11:
        return jsonify({"error": "CPF inválido."}), 400

    novo_cadastro = cadastro(nome, cpf)
    contas.append(novo_cadastro)
    salvar_contas()
    return jsonify({"message": "Conta criada com sucesso!"}), 201

@app.route('/contas/saque', methods=['POST'])
def saque():
    data = request.json
    valor_saque = data.get('valor')
    cpf = data.get('cpf')

    for conta in contas:
        if conta.cpf == cpf:
            if conta.sacar(valor_saque):
                salvar_contas()
                return jsonify({"message": f"Saque de R${valor_saque:.2f} realizado com sucesso."}), 200
            return jsonify({"error": "Saldo insuficiente ou valor inválido."}), 400

    return jsonify({"error": "Conta não encontrada."}), 404

@app.route('/contas/depositar', methods=['POST'])
def deposito():
    data = request.json
    cpf = data.get('cpf')
    valor_deposito = data.get('valor')

    for conta in contas:
        if conta.cpf == cpf:
            if conta.depositar(valor_deposito):
                salvar_contas()
                return jsonify({"message": f"Depósito de R${valor_deposito:.2f} realizado com sucesso."}), 200
            return jsonify({"error": "Valor inválido."}), 400

    return jsonify({"error": "Conta não encontrada."}), 404
