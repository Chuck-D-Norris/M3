class Rectangle:
    def __init__(self, ample, alçada):
        self.ample = ample
        self.alçada = alçada

    def calcularArea(self):
        return self.ample * self.alçada
    

Rectangle1 = Rectangle (5,7)
print(Rectangle1.calcularArea())