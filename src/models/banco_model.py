class cadastro:
    id_contar = 0 #variavel para fazer o aumento autoincremental do id

    def __init__(self, nome, cpf):
        cadastro.id_contar += 1 #autoincrementador de ids
        self.id = cadastro.id_contar #define o id da conta como o contador atual
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def __str__(self): #retorna uma representação em formato string da conta
        return f'ID: {self.id}, Nome: {self.nome}, CPF: {self.cpf}, Saldo: {self.saldo}'

    #calculo para permitir manipulação em forma de deposito do saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            #caso o deposito tenha sido um sucesso ira ser retornado como verdadeiro
            return True 
        return False  

    #calculo para permitir manipulação em forma de saque do saldo
    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                #caso o saque tenha sido um sucesso ira ser retornado como verdadeiro
                return True
            return False 
        return False  
