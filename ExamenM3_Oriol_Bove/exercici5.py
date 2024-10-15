class Figura:
    def calcularArea(self):
        return self.base * self.altura / 2


class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def calcularArea(self):
        return 3.14 * self.radi ** 2

class Triangle(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura / 2

cercle1 = Cercle(5)
print("La area del triangle es:", cercle1.calcularArea())

triangle1 = Triangle(4, 6)
print("La area del triangle es:", triangle1.calcularArea())