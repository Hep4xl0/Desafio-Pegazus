import json
import os
from src.models.banco_model import cadastro

# Define o caminho para o arquivo JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), '../../data/contas.json')

contas = []

def carregar_contas():
    try:
        with open(DATA_FILE, 'r') as f:
            dados = json.load(f)
            for dado in dados:
                novo_cadastro = cadastro(dado['nome'], dado['cpf'])
                novo_cadastro.id = dado['id']  # Load the ID
                novo_cadastro.saldo = dado['saldo']  # Load the balance
                contas.append(novo_cadastro)
    except FileNotFoundError:
        print("Arquivo de contas não encontrado. Iniciando com contas vazias.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Iniciando com contas vazias.")

def salvar_contas():
    with open(DATA_FILE, 'w') as f:
        dados = [{'id': conta.id, 'nome': conta.nome, 'cpf': conta.cpf, 'saldo': conta.saldo} for conta in contas]
        json.dump(dados, f, indent=4)

