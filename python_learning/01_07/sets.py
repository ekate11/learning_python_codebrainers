some_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3,
             3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]

# stworzymy z listy zbior danych:

some_set = set(some_list)
print("Zbior:", some_set, "a jego zbior:", type(some_set))

new_list = list(some_set)
print(new_list)


# in -> True/False
# not in -> True/False

x = 1 in some_set
y = 10 not in some_set
print (x, y)

a = {1, 2, 3}   # ZBIOR
b = {4, 5, 6}

print(a | b) # dodawanie zbiora
print(a - b) # Odejmowanie zbiora
print(a & b) # Mnozenie zbiora

print(a ^ b) # Dzielenie zbiora

# Pytanie na rozmowie: co mozemy zrobic zeby podmienic wartosc w krotce?

