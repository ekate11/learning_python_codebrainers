x = True 
y = False 
n = None 
# == porownania dwoch wartosci
# > wieksze 
# < mniejsze 
# >= wieksze lub rowne
# <= mniejsze lub rowne 
# != rożne
# is to porownanie obiektow, czy sa takie same, czy nie
# in
# not in 
print("Porownanie", 2 == 2)
print("Róznośc dwoch liczb", 2 != 3)
print("Co bedzie tutaj?", '1' == 1)
print("Co bedzie tutaj?", '1' is 1)

a = (2 == 2)
b = (5 < 10)

print("Czy 2 jest rowne 2?", a)
print("Czy 5 jest mniejsze od 10?", b)
print("Typ zmiennej a, to typ:", type(a), "typ zmiennej b, to typ:", type(b))
new_value = str(a)
print("Typ zmiennej new_value, to typ:", type(new_value))
old_list = ['a','b','c']
new_str = str(old_list)
print(new_str, "i jest to typu", type(new_str), "dlugosc", len(new_str))