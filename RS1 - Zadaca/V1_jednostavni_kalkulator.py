def main():
    while True:
        try:
            a = float(input("Unesite prvi broj: "))
            b = float(input("\nUnesite drugi broj: "))
            break
        except ValueError:
            print("Neispravan unos broja.")
    
    
    while True:
        try:
            operator = input("\nUnesite operator (+, -, *, /): ").strip()
            break
        except ValueError:
            print("\nNepodržani operator!")

    if operator == "+":
        res = a + b
    elif operator == "-":
        res = a - b
    elif operator == "*":
        res = a * b
    elif operator == "/":
        if b == 0:
            print("Dijeljenje s nulom nije dozvoljeno.")
            return
        res = a / b

    print(f"Rezultat operacije {a} {operator} {b} je {res}")

if __name__ == "__main__":
    main()