from data.prilog import razredi_studenti

def dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) -> list:
    lista_studenata = []
    
    for element in razredi_studenti:
        if element["razred"] == naziv_razreda:
            for student in element["studenti"]:
                lista_studenata.append(student["ime_prezime"])
    return lista_studenata

def prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float:
    for element in razredi_studenti:
        for student in element["studenti"]:
            if student["ime_prezime"] == ime_prezime:
                ocjene = []
                for kolegij in student["kolegiji"]:
                    ocjene.append(kolegij["ocjena"])
                if ocjene: 
                    return sum(ocjene) / len(ocjene)
                else:
                    return None
    return None

broj_studenata = [(element["razred"], len(element["studenti"])) for element in razredi_studenti]

rezultat = [student["ime_prezime"] 
            for element in razredi_studenti
            if element["razred"] == "1B"
            for student in element["studenti"]
            ]

print(rezultat)
     
def main():
    razred = "1A"
    studenti_iz_razreda = dohvati_studente_iz_razreda(razredi_studenti, razred)
    print(f"Studenti iz razreda {razred}: {studenti_iz_razreda}")       
    
    ime_prezime = "Ivana Kovač"
    prosjek = prosjek_studenta(razredi_studenti, ime_prezime)
    if prosjek is not None:
        print(f"Prosjek ocjena studenta {ime_prezime} je: {prosjek:.2f}")       
    else:
        print(f"Student {ime_prezime} nije pronađen ili nema ocjena.")           

main()