# Program napišite na dva načina: koristeći for i while petlje.

def main():
    while True:
        try:
            n = int(input("Unesite nenegativan cijeli broj za izračun faktorijela: "))
            if n < 0:
                print("Molimo unesite nenegativan broj.")
                continue
            break
        except ValueError:
            print("Neispravan unos. Molimo unesite cijeli broj.")
    
    faktorijel_while = 1
    i = 1
    while i <= n:
        faktorijel_while *= i
        i += 1

    print(f"Faktorijel broja {n} (while petlja) je: {faktorijel_while}")

    faktorijel_for = 1
    for j in range(1, n + 1):
        faktorijel_for *= j

    print(f"Faktorijel broja {n} (for petlja) je: {faktorijel_for}")

if __name__ == "__main__":
    main()