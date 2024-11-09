class Student:
    def __init__(self, ime, prezime, kolegiji):
        self.ime = ime
        self.prezime = prezime
        self.kolegiji = kolegiji

    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}."

    def ispis_kolegija(self):
        return f"Moji kolegiji su: {', '.join(self.kolegiji)}."

    def ispis_ocjena(self, ocjene):
        for kolegij, ocjene in ocjene.items():
            print(f"Ocjene iz kolegija {kolegij}: {', '.join(map(str, ocjene))}.")