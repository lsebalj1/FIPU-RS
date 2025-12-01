from fakultet.podaci import razredi_studenti
from fakultet.student import Student

def popis_studenata(razredi_studenti: list):
    student_lista = []
    for element in razredi_studenti:
        for student in element["studenti"]:
            ime_prezime = student["ime_prezime"]
            ime_prezime_split = ime_prezime.split()
            ime = ime_prezime_split[0]
            prezime = ime_prezime_split[1]
            razred = element["razred"]
            kolegij_ocjene = {
                kolegij["naziv"]: kolegij["ocjena"] 
                for kolegij in student["kolegiji"]
            }
            
            instanca_klase = Student(ime=ime, prezime=prezime, razred=razred, kolegij_ocjene=kolegij_ocjene)
            student_lista.append(instanca_klase)
            
    return student_lista

def main():
    studenti = popis_studenata(razredi_studenti)
    for student in studenti:
        print(student)
        print(f"  Prosjek ocjena: {student.prosjek_ocjena()}")
    
    ana = studenti[0]
    print(f"Prije: {ana}")
    
    ana.promjena_razreda("1B")
    print(f"Nakon promjene: {ana}")    
        
main()
    