from collections import Counter

def brojanje_rijeci(tekst):
    tekst = tekst.lower()
    
    for znak in '.,!?;:"()-':
        tekst = tekst.replace(znak, '')
    
    rijeci = tekst.split()
    brojanje = Counter(rijeci)
    
    return dict(brojanje)

def main():
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    rezultat = brojanje_rijeci(tekst)
    print(rezultat)


if __name__ == "__main__":
    main()