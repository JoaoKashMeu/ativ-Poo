import datetime

class Funcionario:
    def __init__(self, id, sobrenome, nome, data_nascimento, data_admissao, salario):
        self.id = id
        self.sobrenome = sobrenome
        self.nome = nome
        self.data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        self.data_admissao = datetime.datetime.strptime(data_admissao, "%d/%m/%Y")
        self.salario = salario

    def idade(self):
        hoje = datetime.datetime.now()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade

    def tempo_de_casa(self):
        hoje = datetime.datetime.now()
        anos = hoje.year - self.data_admissao.year
        if (hoje.month, hoje.day) < (self.data_admissao.month, self.data_admissao.day):
            anos -= 1
        return anos

    def aumento_de_salario(self):
        tempo = self.tempo_de_casa()
        if tempo < 5:
            self.salario *= 1.02  
        elif tempo < 10:
            self.salario *= 1.05  
        else:
            self.salario *= 1.10  
        return self.salario

    def mostrarFuncionario(self):
        return (f"ID: {self.id}, Sobrenome: {self.sobrenome}, Nome: {self.nome}, "
                f"Idade: {self.idade()} anos, Tempo de casa: {self.tempo_de_casa()} anos, "
                f"Salário: {self.salario:.2f} euros")

funcionario = Funcionario("123", "Alecrim", "João", "08/12/2006", "01/04/2020", 3500)
print(funcionario.mostrarFuncionario())
funcionario.aumento_de_salario()
print("Após aumento:")
print(funcionario.mostrarFuncionario())