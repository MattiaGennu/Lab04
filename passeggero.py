class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.codice_cabina = None

    def assegna_cabina(self, codice_cabina):
        self.codice_cabina = codice_cabina

    def rimuovi_cabina(self):
        self.codice_cabina = None

    def __str__(self):
        if self.codice_cabina:
            return f"{self.codice}: {self.nome} {self.cognome} - Cabina: {self.codice_cabina}"
        return f"{self.codice}: {self.nome} {self.cognome} - Nessuna cabina assegnata"

    def __repr__(self):
        return self.__str__()
