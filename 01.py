import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(Figura):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return 2 * (self.altura + self.largura)

# Programa Principal
figuras = [
    Circulo(5),
    Retangulo(4, 6)
]

for figura in figuras:
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
