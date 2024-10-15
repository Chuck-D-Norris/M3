class Persona:
    def __init__(self, Edat):
        self.Edat = Edat

    def esMajorEdat(self):
        if self.Edat >= 18:
            return print("Es major de edat")
        else:
            return print("Es menor de edat")

persona2 = Persona(18)
persona2.esMajorEdat()





