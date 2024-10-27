import math

def trigonometrija(kut):
  radijani = math.radians(kut) # pretvara kut u radijane
  sinus = math.sin(radijani)
  kosinus = math.cos(radijani)
  tangens = math.tan(radijani)
  return sinus, kosinus, tangens # vraća n-torku s vrijednostima trigonometrijskih funkcija

# Poziv funkcije
kut = 45
sinus, kosinus, tangens = trigonometrija(kut)
print(f"Sinus: {sinus}, Kosinus: {kosinus}, Tangens: {tangens}")