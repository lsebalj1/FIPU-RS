def grupiraj_po_paritetu(lista):
    parni = []
    neparni = []
    
    for broj in lista:
        if broj % 2 == 0:
            parni.append(broj)
        else:
            neparni.append(broj)
    
    rezultat = {
        'parni': parni,
        'neparni': neparni
    }
    
    return rezultat


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rezultat = grupiraj_po_paritetu(lista)
    print(rezultat)


if __name__ == "__main__":
    main()