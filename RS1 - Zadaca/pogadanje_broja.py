def main():
    random_broj = __import__('random').randint(1, 100)
    brojač = 0
    broj_je_pogoden = False

    while not broj_je_pogoden:
        unos = int(input("Pogodi koji je broj između 1 i 100: "))
        brojač += 1

        if unos < 1 or unos > 100:
            print("Uneseni broj nije u dozvoljenom rasponu (1-100). Pokušaj ponovo.")
            continue
        
        if unos < random_broj:
            print("Uneseni broj je manji od traženog broja.")
        elif unos > random_broj:
            print("Uneseni broj je veći od traženog broja.")
        else:
            broj_je_pogoden = True
            print(f"Bravo, pogodio si u {brojač} pokušaja!")

if __name__ == "__main__":
    main()