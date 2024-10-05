from flask import Blueprint, request, render_template
from src.helpers.helper import salvar_contas, contas
from src.models.banco_model import cadastro

# Cria uma blueprint para as rotas do app
app = Blueprint('app', __name__)
#rota para visualizar todas as contas cadastradas
@app.route('/contas', methods=['GET']) #rota inicial
def visualizar_contas():
    return render_template('visu_contas.html', contas=contas) #renderiza as contas no template html visu_contas.html
#rota para criação de contas
@app.route('/contas/criar', methods=['POST', 'GET']) #é usado metodo post para mandar informações para a criação de uma nova conta e get para a renderização do formulario que sera usado para criação da conta
def criar_conta():
    if request.method == 'POST':
        data = request.form #fazer requisição para adquirir as informações do formulario
        #definir as informações do formulario em variaveis para depois aloca-las em uma classe
        nome = data.get('nome')
        cpf = data.get('cpf')
        if cpf.isdigit() and len(cpf) == 11:
            novo_cadastro = cadastro(nome, cpf) #definição dos dados como pertencentes a class cadastro
            contas.append(novo_cadastro) #alocação dentro de um dict que será salvo em um json
            salvar_contas()
            return render_template('visu_contas.html', contas=contas) 
        else:
            return "Erro: CPF inválido", 400
    return render_template('cria_conta.html')
#rota para deposito no saldo da conta
@app.route('/contas/depositar', methods=['POST', 'GET'])
def deposito():
    if request.method == 'POST':
        data = request.form #fazer requisição para adquirir as informações do formulario
        cpf = data.get('cpf')
        valor_deposito = float(data.get('valor'))
        #verificação se o cpf enviado era valido
        for conta in contas:
            if conta.cpf == cpf:
                #realização do deposito atravez do metodo depositar contido na class cadastro
                if conta.depositar(valor_deposito):
                    salvar_contas()
                    return render_template('visu_contas.html', contas=contas)
                return "Erro: Valor inválido.", 400
    return render_template('deposito.html')
#rota para saque do saldo da conta
@app.route('/contas/saque', methods=['POST', 'GET'])
def saque():
    if request.method == 'POST':
        data = request.form #fazer requisição para adquirir as informações do formulario
        cpf = data.get('cpf')
        valor_saque = float(data.get('valor'))
        #verificação se o cpf enviado era valido
        for conta in contas:
            if conta.cpf == cpf:
                #realização do saque atravez do metodo sacar contido na class cadastro
                if conta.sacar(valor_saque):
                    salvar_contas()
                    return render_template('visu_contas.html', contas=contas)
                return "Erro: Saldo insuficiente ou valor inválido.", 400
    return render_template('saque.html')
