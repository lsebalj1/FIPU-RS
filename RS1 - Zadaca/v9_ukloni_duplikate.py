def ukloni_duplikate(lista):
    nova_lista = []
    for broj in lista:
        if broj not in nova_lista:
            nova_lista.append(broj)
    return nova_lista

def main():
    lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(ukloni_duplikate(lista))

if __name__ == "__main__":
    main()