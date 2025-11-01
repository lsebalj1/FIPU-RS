def filtriraj_parne(lista):
    for broj in lista:
        if broj%2 == 0:
            print(broj)
    
def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filtriraj_parne(lista))

if __name__ == "__main__":
    main()

