import json
from src.models.banco_model import cadastro

contas = []

def carregar_contas():
    try:
        with open('contas.json', 'r') as f:
            dados = json.load(f)
            for dado in dados:
                novo_cadastro = cadastro(dado['nome'], dado['cpf'])
                contas.append(novo_cadastro)
    except FileNotFoundError:
        print("Arquivo de contas não encontrado. Iniciando com contas vazias.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Iniciando com contas vazias.")

def salvar_contas():
    with open('contas.json', 'w') as f:
        dados = [{'nome': conta.nome, 'cpf': conta.cpf} for conta in contas]
        json.dump(dados, f, indent=4)
