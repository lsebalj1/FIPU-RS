def while_suma_parnih_brojeva():
    print("\nWhile suma parnih brojeva")
    suma = 0

    i = 2
    while i <= 100:
        suma += i
        i += 2
        
    print(f"\nSuma parnih brojeva je: {suma}")


def for_suma_parnih_brojeva():
    print("\nFor suma parnih brojeva")
    suma = 0

    for i in range(2, 101, 2):
        suma += i 

    print(f"\nSuma parnih brojeva je: {suma}")


def while_deset_neparnih_brojeva():
    print("\nWhile deset neparnih brojeva obratno")
    i = 19

    while i >= 1:
        print(i)
        i -= 2


def for_deset_neparnih_brojeva():
    print("\nFor deset neparnih brojeva obratno")

    for i in range(19, 0, -2):
        print(i)


def while_fibonaccijev_niz():
    print("\nWhile Fibonaccijev niz")
    a = 0
    b = 1

    while a <= 1000:
        print(a)
        a, b = b, a + b  


def for_fibonaccijev_niz():
    print("\nFor Fibonaccijev niz")
    a = 0
    b = 1

    for _ in range(1000):  
        if a > 1000:
            break
        print(a)
        a, b = b, a + b     


def main():
    while_suma_parnih_brojeva()
    for_suma_parnih_brojeva()
    while_deset_neparnih_brojeva()
    for_deset_neparnih_brojeva()
    while_fibonaccijev_niz()
    for_fibonaccijev_niz()


if __name__ == "__main__":
    main()