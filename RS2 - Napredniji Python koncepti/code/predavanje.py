from math import pi

# dictionairy

osoba = {
    "ime": "Marko",
    "prezime": "Marković",
    2: "Pero",
    (1, 2, 3): False
    
}

for kljuc, vrijednost in osoba.items():
    print(f"{kljuc}: {vrijednost}") 

lista = [20, 30, 40, 50, 60]
skup = {1, 2, 3, 4, 5}

for index, vrijednost in enumerate(lista):
    print(f"Index: {index}, Vrijednost: {vrijednost}")

for index, vrijednost in enumerate(skup):
    print(f"Index: {index}, Vrijednost: {vrijednost}")

#lambda

def kvadriraj(x : int):
    return x ** 2

lambda x : x ** 2

kvadriraj = lambda x: x ** 2
print(type(kvadriraj))

print((lambda x, y : (x + y) ** 2)(1, 2))

def funkcija(ime):
    return f"Pozdrav, {ime}!"

funkcija_2 = lambda ime: f"Pozdrav, {ime}!"

def povrsina(r: float) -> float:
    return pi * r ** 2

povrsina_lambda = lambda r: pi * r ** 2

def kont(x: str, y:str) -> str:
    return x + y

def kont_lambda(x: str, y: str) -> str:
    return (lambda a, b: a + b)(x, y)

#funkcija koja ce primjeniti drugu funkciju na svaki element liste
def primjeni_na_sve(lista: list, funkcija: callable):
    nova_lista = []
    for element in lista:
        nova_vrijednost = funkcija(element)
        nova_lista.append(nova_vrijednost)

def uvecaj_pa_kvadriraj(x):
    return (x + 1) ** 2

lista = [1, 2, 3, 4, 5]
print(primjeni_na_sve(lista, uvecaj_pa_kvadriraj))
print(primjeni_na_sve(lista, lambda x: (x + 1) ** 2))

broj = 10
f = lambda x: x**2 if x%2 == 0 else x**3
print(f(broj))

def pomnozi_s_faktorom(faktor: int):
    return lambda x: x * faktor

broj = pomnozi_s_faktorom(5)
print(broj)
print(type(broj))

# map(function, iterables)

lista = [1, 2, 3, 4, 5]

def kubiraj (x:int):
    return x ** 3

map_kubiraj = map(kubiraj, lista)
print(list(map_kubiraj))

def kubiraj_lambda(x:int):
    return (lambda x: x ** 3)(x)

print(list(map(lambda x: x ** 3, lista)))

lista_stringova = ["pero", "marko", "sanja", "josip"]

print(list(map(lambda ime: len(ime), lista_stringova)))


#map funkcija koja vraca listu duljina imena
studenti = [
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0012345678", "godina_rodenja": 2000},
    {"ime": "Pero", "prezime": "Perić", "jmbag": "0012345679", "godina_rodenja": 1999},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0012345680", "godina_rodenja": 2002},
]

print(list(map(lambda student: student["jmbag"], studenti)))

#filter(function, iterable)
# expression mora bit bool, filter vraca reduciranu verziju iterablea

print(list(filter(lambda x: x % 2 == 0, lista)))

print(list(map(lambda x: x % 2 == 0, lista)))

# podskup studenata koji s u ispod 2001
print(list(filter(lambda student: student["godina_rodenja"] < 2001, studenti)))

#funkcija any i all
#any (iterables) true ako je barem jedan istinit element
#all (iterables) true ako su svi elementi istiniti

print(any([False, False, True])) #true
print(all([True, True, True])) #true
print(all([True, False, True])) #false

lista_brojeva = [2, 4, 7, 11, 13, 15, 16]
print(any(map(lambda broj: broj % 2 == 0, lista_brojeva)))
print(all(map(lambda broj: broj % 2 == 0, lista_brojeva)))

putnici = [
    {"ime": "Marko", "prezime": "Marković", "uplata": True},
    {"ime": "Ana", "prezime": "Anić", "uplata": True},          
    {"ime": "Pero", "prezime": "Perić", "uplata": False},
]

print(all(map(lambda putnik: putnik["uplata"], putnici)))
print(list(map(lambda putnik: putnik["uplata"] == True, putnici)))
#map jer ne smijem reducirati s filterom, treba sve ispisati

#reduce funkcija
#gotove funkcije sum, min, max, etc.
from functools import reduce        
lista_brojeva = [1, 2, 3, 4, 5]
zbroj = reduce(lambda x, y: x + y, lista_brojeva)
print(zbroj)

#list comprehensions
brojevi = [1, 2, 3, 4, 5]
kvadrati = map(lambda x: x ** 2, brojevi)
print(list(kvadrati))
# rezultat = [expression for element in iterable]
kvadrati_c = [element ** 2 for element in brojevi]
print(kvadrati_c)

nizovi = ["ana", "pero", "marko", "ivan"]

nizovi_map = map(lambda x: len(x), nizovi)
print(nizovi_map)

nizovi_comp = [len(x) for x in nizovi]
print(nizovi_comp)

#tuple comprehensions
tuple_brojevi = (1, 2, 3, 4, 5)
kvadrati_tuple = tuple(element ** 2 for element in tuple_brojevi)
print(kvadrati_tuple)

brojevi_set = {3, 4, 5, 6, 7, 8}

#transformacija kvadrat neparnih brojeva u set
nova = filter(lambda x: x%2 == 0, brojevi_set)
print(list(map(lambda x: x ** 2, nova)))

rezultat_set = {element ** 2 for element in brojevi_set if element % 2 == 0}
print(rezultat_set)





