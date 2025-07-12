number_list = []
print("Zawartosc listy:", number_list)
print("Dlugosc listy:", len(number_list))

number_list1 = [0 ,1, 2, 3, 4, 5]
print("Zawartosc listy:", number_list1)
print("Dlugosc listy:", len(number_list1))
print("Wycinek listy - ostatni element:", number_list1[-1])
print("Wycinek listy:", type(number_list1[2:1:1]))
number_list1[3] = 10
print(number_list1)

number_list2 = [1, 2, 3, 4]
string_list = ["a", "b", "c", "d"]

new_list = number_list2 + string_list
print(new_list)

# Dodawanie elementow do listy
new_list.append(6)
print(new_list)

# Numer indeksu z listy:

print(new_list.index('d'))


new_list[7]= "nowy_element"
print(new_list)

#Sciagamy element z listy:

new_list.pop()              # usuwa ostatni element
print(new_list)

# Szukanie elementu w liscie

print("a" in new_list)
print("w" in new_list)

#Czy lista jest pusta

print(len(new_list))
print(len(""))


a = 0
b = []
c = ""
flag = 0


unsorted_list = [12,3,2,4,7,1]
unsorted_list.sort()
print ("Posortowana lista:", unsorted_list)

# Odwracanie listy:

unsorted_list.reverse()
print ("Odwrocona lista:", unsorted_list)

mixed_list = ['1', 'b', 'c', '3.14', 'tekst', '14124141', '111', '222', '131231']
mixed_list.sort(reverse=True)
print ("Odwrocona lista:", mixed_list)


# Listy zagniezdzone
macierz = [[0,1,2,3],
           [4,5,6],
           [7,8,9]]
print(len(macierz))     # Dlugosc macierzy
print(len(macierz[0]))      # Dlugosc wycinka macierzy

lista_uzytkownikow = ['Jan',
                      'Anna',
                      'Piotr']

print(len(lista_uzytkownikow))

macierz[0].reverse()
print("Odwrocona macierz:", macierz)