class Cabina:
    def __init__(self, codice, letti, ponte, prezzo_base):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzo_base = float(prezzo_base)
        self.disponibile = True

    def prezzo_finale(self):
        return round(self.prezzo_base, 2)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"{self.codice}: Standard | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo_finale():.2f}€ - {stato}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if not isinstance(other, Cabina):
            return NotImplemented
        if self.prezzo_finale() == other.prezzo_finale():
            return self.codice < other.codice
        return self.prezzo_finale() < other.prezzo_finale()

    def __eq__(self, other):
        if not isinstance(other, Cabina):
            return NotImplemented
        return self.codice == other.codice


class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, max_animali):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.max_animali = int(max_animali)

    def prezzo_finale(self):
        prezzo = self.prezzo_base * (1 + 0.10 * self.max_animali)
        return round(prezzo, 2)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return (f"{self.codice}: Animali | {self.letti} letti - Ponte {self.ponte} - "
                f"Prezzo {self.prezzo_finale():.2f}€ - Max animali: {self.max_animali} – {stato}")


class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo_base, stile):
        super().__init__(codice, letti, ponte, prezzo_base)
        self.stile = stile

    def prezzo_finale(self):
        prezzo = self.prezzo_base * 1.20
        return round(prezzo, 2)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return (f"{self.codice}: Deluxe ({self.stile}) | {self.letti} letti - Ponte {self.ponte} - "
                f"Prezzo {self.prezzo_finale():.2f}€ – {stato}")
