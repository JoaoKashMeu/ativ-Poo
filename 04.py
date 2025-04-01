class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        elif valor <= 0:
            print("Erro: O valor do saque deve ser positivo!")
        else:
            self.__saldo -= valor

    def exibir_saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        if novo_titular.strip() == "":
            print("Erro: Nome do titular não pode ser vazio!")
        else:
            self.__titular = novo_titular

    def __str__(self):
        return f"Conta de {self.__titular} com saldo de {self.__saldo:.2f} reais"

conta = ContaBancaria("João", 1000)
print(conta)  

conta.depositar(500)  
print(conta.exibir_saldo())  

conta.sacar(2000)  
conta.sacar(300)  
print(conta.exibir_saldo())  

conta.titular = ""  
conta.titular = "Maria"  
print(conta)  