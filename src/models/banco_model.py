class cadastro:
    id_contar = 0

    def __init__(self, nome, cpf):
        cadastro.id_contar += 1
        self.id = cadastro.id_contar
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def __str__(self):
        return f'ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, Saldo: {self.saldo}'

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False  

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                return True
            return False 
        return False  
