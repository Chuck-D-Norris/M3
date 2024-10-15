class Llibre:
    def __init__(self, titol, autor, genere):
        self.titol = titol
        self.autor = autor
        self.genere = genere

    def mostrar_dades(self):
        return f"Titol: {self.titol}, Autor: {self.autor}, Any: {self.any}"
    

class Usuari:
    def __init__(self, Identificaro, Nom):
        self.Identificaro = Identificaro
        self.Nom = Nom

    def mostrar_dades(self):
        return f"Identificaro: {self.Identificaro}, Nom: {self.Nom}"
    

class Bilbioteca:
    def __init__(self, llibres, usuaris):
        self.llibres = llibres
        self.usuaris = usuaris



        