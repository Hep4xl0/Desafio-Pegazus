import json
import os
from src.models.banco_model import cadastro

# Define o caminho para o arquivo JSON
LOCAL = os.path.join(os.path.dirname(__file__), '../../data/contas.json')
#lista que armazenará as contas carregas do arquivo json
contas = []
#função que ira carregar as contas armazenadas no arquivo json
def carregar_contas():
    #abre os arquivos json em forma de leitura
    with open(LOCAL, 'r') as f:
        #carrega os dados do json em uma variavel
        dados = json.load(f)
        for dado in dados:
            #criando um cadastro baseado nos dados do arquivo json
            novo_cadastro = cadastro(dado['nome'], dado['cpf'])
            novo_cadastro.id = dado['id']
            novo_cadastro.saldo = dado['saldo']
            contas.append(novo_cadastro) #armazena a variavel em um dic

#salva os dados no arquivo json
def salvar_contas():
    #abertura do arquivo em modo de escrita
    with open(LOCAL, 'w') as f:
        #define o dicionario e sua formatação para ser salvo no json
        dados = [{'id': conta.id, 'nome': conta.nome, 'cpf': conta.cpf, 'saldo': conta.saldo} for conta in contas]
        #escreve os dados no arquivo json
        json.dump(dados, f, indent=4)

