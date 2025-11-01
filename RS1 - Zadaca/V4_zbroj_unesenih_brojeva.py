def main():
    sum = 0

    while True:
        unos = int(input("Unesite broj: (0 za kraj)"))

        if unos == 0:
            break
        sum += unos

    print(f"Zbroj svih prethodno unesenih brojeva: {sum}")

if __name__ == "__main__":
    main()