from flask import Blueprint, request, render_template
from src.helpers.helper import salvar_contas, contas
from src.models.banco_model import cadastro

# Create a Blueprint for routes
app = Blueprint('app', __name__)

@app.route('/contas', methods=['GET'])
def visualizar_contas():
    return render_template('visu_contas.html', contas=contas)

@app.route('/contas/criar', methods=['POST', 'GET'])
def criar_conta():
    if request.method == 'POST':
        data = request.form
        nome = data.get('nome')
        cpf = data.get('cpf')
        if cpf.isdigit() and len(cpf) == 11:
            novo_cadastro = cadastro(nome, cpf)
            contas.append(novo_cadastro)
            salvar_contas()
            return render_template('visu_contas.html', contas=contas)
        else:
            return "Erro: CPF inválido", 400
    return render_template('cria_conta.html')

@app.route('/contas/depositar', methods=['POST', 'GET'])
def deposito():
    if request.method == 'POST':
        data = request.form
        cpf = data.get('cpf')
        valor_deposito = float(data.get('valor'))
        for conta in contas:
            if conta.cpf == cpf:
                if conta.depositar(valor_deposito):
                    salvar_contas()
                    return render_template('visu_contas.html', contas=contas)
                return "Erro: Valor inválido.", 400
    return render_template('deposito.html')

@app.route('/contas/saque', methods=['POST', 'GET'])
def saque():
    if request.method == 'POST':
        data = request.form
        cpf = data.get('cpf')
        valor_saque = float(data.get('valor'))
        for conta in contas:
            if conta.cpf == cpf:
                if conta.sacar(valor_saque):
                    salvar_contas()
                    return render_template('visu_contas.html', contas=contas)
                return "Erro: Saldo insuficiente ou valor inválido.", 400
    return render_template('saque.html')
