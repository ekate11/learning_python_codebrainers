# Zadanie 1 suma dwoch liczb 
# Inicjalizuj sumę = 0, num1 = 10, num2 = 20 (PROCES)
# Wprowadź liczby (I / O)
# Dodaj je i zapisz wynik w sumie (PROCES)
# Wydrukuj sumę (I / O)

suma = 0
number1 = 10
number2 = 20
suma = number1 + number2
print ("suma:", suma)



# Zadanie 2 Konwersja temperatury z Fahrenhaita na Celcjusza, oraz na Kelvina
# Zainicjalizuj temp w Farh
# Zainicjalizuj temp w Celcjuszach jako nowa zmienna np: temp_cel i przypisz do niej wynik konwersji 
# Zainicalizuj temp w Kelwinach jako nowa zmienna np: temp_kel i przypisz do niej wynik konwersji

print ("Konwersja temperatury")
temp_fahr = 100
kelvin_offset = 273.15
fahr_to_cel = 5/9
fahr_constant = 32

print("Temperatura w Fahr:", temp_fahr)
temp_cel = (temp_fahr - fahr_constant)*fahr_to_cel
print ("Temperatura w Cels:", temp_cel)
temp_kel = temp_cel + kelvin_offset
print ("Temperatura w Kelvinach:", temp_kel)
