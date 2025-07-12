interable_element = 'Codebrainers'
interable_element = ("C", "o", "d", "e")
#interable_element = list(interable_element) 

i = 0
for element in interable_element:
    print("Litera:", element, ["przebieg pietli", i])
    i +=1
    if element == 'o':
        print("o!")

# Drukowanie wartosci slownika:

iterable_dictionary = {"C": 1, "o": 2, "d": 3, "e":4}
for element in iterable_dictionary:
    print("Element slownika", iterable_dictionary[element])

for key, value in iterable_dictionary.items():
    print("Klucz", key, "Wartosc", value)

#zaduzo nawiasow stworzyli krotke(tuple):
for key, value in iterable_dictionary.items():
    print(("Klucz", key, "Wartosc", value))


#range() #generuje liczbe calkowita pomiedzy jedna a druga liczba
# zawsze bedzie iterowac od 0!
for x in range(10):
    print("iks =", x)


a = 10
for i in range(0,10):
    print("Przebieg petli=", i)