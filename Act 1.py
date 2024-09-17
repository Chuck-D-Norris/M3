class Fill():
    def __init__(self, NomFill):
        self.NomFill = NomFill

        


class Pare (Fill):
    def __init__(self,PrimeCognom, segonCognom, Nom,):
        self.PrimeCognom = PrimeCognom
        self.segonCognom = segonCognom
        self.Nom = Nom

        
        



class Mare(Fill):
    def __init__(self, PrimeCognom, segonCognom, Nom):
        self.PrimeCognom = PrimeCognom
        self.segonCognom = segonCognom
        self.Nom = Nom


Fill = Fill("Xavi")
print(Fill)