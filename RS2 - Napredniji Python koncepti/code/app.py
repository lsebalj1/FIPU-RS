from faculty import studenti, operacije

student_marko = studenti.Student("Marko", "Marković", ["Web aplikacije", "Raspodijeljeni sustavi", "Operacijska istraživanja"])

ocjene_studenta = operacije.ocjene(student_marko.kolegiji)

print(ocjene_studenta) # {'Web aplikacije': [], 'Raspodijeljeni sustavi': [], 'Operacijska istraživanja': []}

simulacija_ocjena = operacije.simuliraj_ocjene(student_marko.kolegiji) # {'Web aplikacije': [2, 3, 1, 4, 4], 'Raspodijeljeni sustavi': [3, 1, 3, 4, 1], 'Operacijska istraživanja': [5, 2, 1, 1, 5]}

print(simulacija_ocjena)

######

student_marko.ispis_ocjena(simulacija_ocjena)