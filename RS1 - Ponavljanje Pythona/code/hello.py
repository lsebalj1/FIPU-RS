tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels_count = 0
    consonants_count = 0
    for letter in tekst:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonants:
            consonants_count += 1
    return dict(vowels=vowels_count, consonants=consonants_count) 

print(count_vowels_consonants(tekst))