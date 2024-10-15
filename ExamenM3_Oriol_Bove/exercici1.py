class Persona:
    def __init__(self, Nom):
        self.Nom = Nom



    def saludar(self):
        print("Bon Dia", self.Nom)


persona = Persona("Musolini")
persona.saludar()
    