# Zadanie 3: Napisz program liczący zysk z konta oszczędnościowego.
# Dla przypisanego do zmiennych wartości: kwota początkowa, lata, oprocentowanie
# Oblicz kwotę zysku po upływie określonej liczby lat i wyświetl wynik.
#       - program powinien mieć 3 zmienne: `kwota, miesiace, oprocentowanie`
#       - zakładamy roczną kapitalizację odsetek oraz brak podatku belki.
#       - dla danych: `kwota = 10000, lat = 3, oprocentowanie = 8` poprawny wynik
#         to `2597.12`
#       - dla danych: 100 zł, 2 lat, oprocentowania 7% matematyczny wzór to: 100 * 1,07^2

print("Zadanie 3: Oblicz zysk z konta oszczędnościowego")
kwota_poczatkowa = int(input ("Podaj kwote poczatkowa:")) # Kwota początkowa
lata = int(input ("Podaj ilosc lat:") )# Liczba lat
oprocentowanie = int(input ("Podaj oprocentowanie w %:") )# Oprocentowanie w %
zysk = kwota_poczatkowa * (1 + oprocentowanie / 100) ** lata - kwota_poczatkowa
print("Zysk po", lata, "latach wynosi:", round(zysk, 2))    