def main():
    while True:
        try:
            godina = int(input("Unesite godinu:"))
            break
        except ValueError:
            print("Neispravan unos godine.")
    
    if(godina % 4 == 0 and godina % 100 != 0 or godina % 400 == 0):
        print(f"Godina {godina} je prijestupna.")
    else:
        print(f"Godina {godina} nije prijestupna.")

if __name__ == "__main__":
    main()