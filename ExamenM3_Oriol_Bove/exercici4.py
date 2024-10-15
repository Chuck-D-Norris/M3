class Persona:
    def __init__(self, nom):
        self.nom = nom
        
    def saludar(self):
        print("Bon dia hem dic", self.nom)


class Empleat(Persona):
    def __init__(self, nom, salari):
        super().__init__(nom)
        self.salari = salari

    def saludar2(self):
        print("Hola, sóc", self.nom, "la miseria meua es", self.salari)



empleat1 = Empleat("Adolf", 300)
empleat1.saludar()
empleat1.saludar2()