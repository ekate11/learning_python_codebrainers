# funkcja wywoluje sama siebie

def suma_mn(number):
    """
    dzialajaca funkcja
    """

    suma = 0
    for i in range(number + 1):
        suma = suma + i
        print( "#Wartosc i =",i,  "Suma=", suma)
    return suma

print(suma_mn(3))



# rekursja 

def suma_rek(number):
    if number == 0:
        return 0
    print("Number =", number)
    return number + suma_rek(number - 1)

print(suma_rek(3))