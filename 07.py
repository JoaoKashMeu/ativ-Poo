class Categoria:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Categoria: {self.nome}"


class Avaliacao:
    def __init__(self, cliente, comentario, nota):
        self.cliente = cliente
        self.comentario = comentario
        self.nota = nota

    def __str__(self):
        return f"Avaliação de {self.cliente}: {self.comentario} - Nota: {self.nota}"


class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.categoria = categoria
        self.__avaliacoes = []

    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
            print(f"{quantidade} unidade(s) vendida(s) de {self.__nome}.")
        else:
            print(f"Estoque insuficiente para {self.__nome}.")

    def reabastecer(self, quantidade):
        self.__estoque += quantidade
        print(f"{quantidade} unidade(s) adicionada(s) ao estoque de {self.__nome}.")

    def adicionar_avaliacao(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def detalhes(self):
        detalhes_produto = f"Produto: {self.__nome}\nPreço: R${self.__preco:.2f}\nEstoque: {self.__estoque}\n{self.categoria}\n"
        if self.__avaliacoes:
            detalhes_produto += "Avaliações:\n" + "\n".join(str(avaliacao) for avaliacao in self.__avaliacoes)
        else:
            detalhes_produto += "Sem avaliações ainda."
        return detalhes_produto

    def __str__(self):
        return f"Produto: {self.__nome} - Preço: R${self.__preco:.2f}"


class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []  

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_estoque(self):
        print(f"Estoque da loja {self.nome}:")
        for produto in self.produtos:
            print(f"{produto} - Estoque: {produto._Produto__estoque}")

    def __str__(self):
        return f"Loja: {self.nome}"

if __name__ == "__main__":
    eletronicos = Categoria("Eletrônicos")
    livros = Categoria("Livros")

    celular = Produto("Celular", 1500.00, 10, eletronicos)
    livro = Produto("Livro Python", 100.00, 5, livros)

    loja = Loja("Tech & Books")

    loja.adicionar_produto(celular)
    loja.adicionar_produto(livro)

    celular.vender(2)
    livro.reabastecer(3)

    avaliacao1 = Avaliacao("João", "Ótimo produto!", 5)
    celular.adicionar_avaliacao(avaliacao1)

    loja.listar_estoque()

    print("\nDetalhes do produto:")
    print(celular.detalhes())
