import os
from cabina import Cabina, CabinaAnimali, CabinaDeluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self._cabine = {}
        self._passeggeri = {}
    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File non trovato: {file_path}")
        self._cabine.clear()
        self._passeggeri.clear()
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 0:
                    continue
                codice = parts[0]

                if codice.upper().startswith("CAB"):

                    if len(parts) < 4:

                        continue
                    _, letti, ponte, prezzo = parts[0:4]
                    if len(parts) == 4:
                        cab = Cabina(codice, letti, ponte, prezzo)
                    else:
                        extra = parts[4]

                        if extra.isdigit():
                            cab = CabinaAnimali(codice, letti, ponte, prezzo, int(extra))
                        else:
                            cab = CabinaDeluxe(codice, letti, ponte, prezzo, extra)
                    self._cabine[codice] = cab

                elif codice.upper().startswith("P"):

                    if len(parts) < 3:
                        continue
                    _, nome, cognome = parts[0:3]
                    passeggero = Passeggero(codice, nome, cognome)
                    self._passeggeri[codice] = passeggero

                else:
                    continue
    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        if codice_cabina not in self._cabine:
            raise Exception(f"Cabina '{codice_cabina}' non trovata.")
        if codice_passeggero not in self._passeggeri:
            raise Exception(f"Passeggero '{codice_passeggero}' non trovato.")
        cab = self._cabine[codice_cabina]
        pas = self._passeggeri[codice_passeggero]
        if not cab.disponibile:
            raise Exception(f"La cabina {codice_cabina} non è disponibile.")
        if pas.codice_cabina is not None:
            raise Exception(f"Il passeggero {codice_passeggero} ha già la cabina {pas.codice_cabina} assegnata.")

        cab.disponibile = False
        pas.assegna_cabina(codice_cabina)
    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        lista = list(self._cabine.values())
        lista.sort()
        return lista

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for codice in sorted(self._passeggeri.keys()):
            p = self._passeggeri[codice]
            if p.codice_cabina:
                print(f"{p.codice}: {p.nome} {p.cognome} - Cabina: {p.codice_cabina}")
            else:
                print(f"{p.codice}: {p.nome} {p.cognome} - Nessuna cabina assegnata")

    def get_cabine(self):
        return dict(self._cabine)

    def get_passeggeri(self):
        return dict(self._passeggeri)