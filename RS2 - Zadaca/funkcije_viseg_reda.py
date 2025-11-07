#1
nizovi = ["jabuka", "kruška", "banana", "naranča"]

print(list(map(lambda x: (len(x) ** 2), nizovi)))

#2
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

print(list(filter(lambda x: x > 5, brojevi)))

#3
brojevi_2 = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x, x ** 2), brojevi_2))

print(transform)

#4
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda student:  student >= 18, studenti["godine"]))
print(svi_punoljetni)


