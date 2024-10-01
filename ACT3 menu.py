class Compte:
    def __init__(self, nom, telefon, email, quantitat):
        self.nom = nom
        self.telefon = telefon
        self.email = email
        self.quantitat = quantitat

    def mostrar_dades(self):
        return f"Nom: {self.nom}, Telèfon: {self.telefon}, Email: {self.email}, Quantitat: {self.quantitat}"

class Fixe(Compte):
    def __init__(self, nom, telefon, email, quantitat, plaç, interès):
        super().__init__(nom, telefon, email, quantitat)
        self.plaç = plaç
        self.interès = interès

    def obtenir_interès(self):
        return (self.quantitat * self.interès) / 100

    def mostrar_informacio(self):
        total = self.quantitat + self.obtenir_interès()
        return (f"{self.mostrar_dades()}, Plaç: {self.plaç}, "
                f"Interès: {self.interès}%, Total: {total}")

class Estalvi(Compte):
    def mostrar_estalvis(self):
        return f"Estalvis: {self.quantitat}"

# Funcions per al menú
def afegir_client(clients):
    nom = input("Nom del client: ")
    telefon = input("Telèfon del client: ")
    email = input("Email del client: ")
    quantitat = float(input("Quantitat de diners: "))
    tipus = input("Tipus de compte (Fixe/Estalvi): ").lower()

    if tipus == "fixe":
        plaç = int(input("Plaç: "))
        interès = float(input("Interès: "))
        client = Fixe(nom, telefon, email, quantitat, plaç, interès)
    elif tipus == "estalvi":
        client = Estalvi(nom, telefon, email, quantitat)
    else:
        print("Tipus de compte no vàlid.")
        return

    clients.append(client)
    print("Client afegit amb èxit.")

def llistar_clients(clients):
    if not clients:
        print("No hi ha clients enregistrats.")
        return
    for i, client in enumerate(clients):
        print(f"{i + 1}. {client.mostrar_dades()}")

def mostrar_dades_client(clients):
    index = int(input("Introdueix el número del client per mostrar les dades: ")) - 1
    if 0 <= index < len(clients):
        if isinstance(clients[index], Fixe):
            print(clients[index].mostrar_informacio())
        else:
            print(clients[index].mostrar_estalvis())
    else:
        print("Client no vàlid.")

def buscar_client(clients):
    nom = input("Introdueix el nom del client a buscar: ")
    for client in clients:
        if client.nom.lower() == nom.lower():
            print(client.mostrar_dades())
            return
    print("Client no trobat.")

def modificar_client(clients):
    index = int(input("Introdueix el número del client a modificar: ")) - 1
    if 0 <= index < len(clients):
        client = clients[index]
        client.nom = input("Nou nom (deixa en blanc per mantenir): ") or client.nom
        client.telefon = input("Nou telèfon (deixa en blanc per mantenir): ") or client.telefon
        client.email = input("Nou email (deixa en blanc per mantenir): ") or client.email
        quantitat = input("Nova quantitat (deixa en blanc per mantenir): ")
        if quantitat:
            client.quantitat = float(quantitat)

        print("Client modificat amb èxit.")
    else:
        print("Client no vàlid.")

def eliminar_client(clients):
    index = int(input("Introdueix el número del client a eliminar: ")) - 1
    if 0 <= index < len(clients):
        clients.pop(index)
        print("Client eliminat amb èxit.")
    else:
        print("Client no vàlid.")

def menu():
    clients = []
    while True:
        print("\nMenú:")
        print("1. Afegir un client")
        print("2. Llistar clients")
        print("3. Mostrar les dades d'un client")
        print("4. Buscar client")
        print("5. Modificar un client")
        print("6. Eliminar un client")
        print("7. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            afegir_client(clients)
        elif opcio == "2":
            llistar_clients(clients)
        elif opcio == "3":
            mostrar_dades_client(clients)
        elif opcio == "4":
            buscar_client(clients)
        elif opcio == "5":
            modificar_client(clients)
        elif opcio == "6":
            eliminar_client(clients)
        elif opcio == "7":
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida.")

# Crear alguns clients per a la prova
clients = [
    Fixe("Joan", "600000001", "joan@example.com", 1000, 12, 3.5),
    Estalvi("Maria", "600000002", "maria@example.com", 2000)
]

# Iniciar el menú
menu()
    