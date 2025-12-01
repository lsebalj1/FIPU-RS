from fakultet.podaci import razredi_studenti

class Student:
    def __init__(self, ime: str, prezime: str, razred: str, kolegij_ocjene: dict):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.kolegij_ocjene = kolegij_ocjene

    def __str__(self):
        return f"Student: {self.ime} {self.prezime}, Razred: {self.razred}, Kolegiji i ocjene: {self.kolegij_ocjene}"
    
    def prosjek_ocjena(self) -> float:
        if not self.kolegij_ocjene: 
            return 0.0
        prosjek = sum(self.kolegij_ocjene.values()) / len(self.kolegij_ocjene)
        return round(prosjek, 1)
    
    def promjena_razreda(self, novi_razred: str) -> None:
        mogući_razredi = [element["razred"] for element in razredi_studenti]
        
        if novi_razred not in mogući_razredi:
            raise ValueError(f"Razred {novi_razred} nije dopušten.")
        
        self.razred = novi_razred
