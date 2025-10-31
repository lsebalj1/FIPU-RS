broj = 0
while broj < 5:
broj +=2
print(broj)

# Rezultat će biti:
# 2 
# 4
# 6

broj = 0
while broj < 5:
broj += 1
print(broj)
broj -= 1

# Petlja je beskonačna jer se vrijednost varijable broj povecava i smanjuje za 1 unutar petlje, 
# stoga će petlja beskonačno ispisivati broj 1.

broj = 10
while broj > 0:
broj -= 1
print(broj)
if broj < 5:
broj += 2

# Ono što ne valja s petljom je to što se vrijednost varijable broj može povećati unutar petlje i ići iznad početne vrijednosti 10.

