class Dad:
    def __init__(self, firstName="Josep", lastName="Fibla Armengol"):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"

class Mom:
    def __init__(self, firstName="Maria", lastName="Agustín Franch"):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"

class Child:
    def __init__(self, firstName, dad=None, mom=None):
        self.firstName = firstName
        self.dad = dad if dad else Dad()
        self.mom = mom if mom else Mom()

    def getFullName(self):
        return f"{self.firstName} {self.dad.lastName.split()[0]} {self.mom.lastName.split()[0]}"

    def getDadFullName(self):
        return self.dad.getFullName()

    def getMomFullName(self):
        return self.mom.getFullName()

# Test
child = Child("Xavi")
print(child.getFullName())
print(child.getDadFullName())
print(child.getMomFullName())
