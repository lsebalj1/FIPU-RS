def provjeri_lozinku():
    while True:
        lozinka = input("Unesite lozinku: ")
        
        if len(lozinka) < 8 or len(lozinka) > 15:
            print("Lozinka mora sadržavati između 8 i 15 znakova")
            continue
        if not any(c.isupper() for c in lozinka) or not any(c.isdigit() for c in lozinka):
            print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
            continue
        if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
            print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
            continue
        
        print("Lozinka je jaka!")
        break

def main():
    provjeri_lozinku()

if __name__ == "__main__":
    main()