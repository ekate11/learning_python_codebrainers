
def add_two_numbers(x,y):
    """
    Funkcja dodaje dwie liczby
    :param x: liczba calkowita lub rzeczewista
    :param y: liczba calkowita lub rzeczewista
    """
    return x + y
    

print("Suma = ", add_two_numbers(10,20))
print("Suma = ", add_two_numbers(20,20))
print("Suma = ", add_two_numbers(30,20))
print("Suma = ", add_two_numbers(40,20))

print(add_two_numbers(2,8))

# build in funktions in python

print(sum([10,40,6,7,45]))

print(max([5, 9,47,89]))


def funktion1(a, b, c, d, e = 0):
    e = 0
    pass

funktion1(1, 2, 3, 4, 5) # NADPISANIE WARTOSCI DOMYSLNEJ e = 0 PRZEZ 5

