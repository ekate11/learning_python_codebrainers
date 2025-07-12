d = {} # slownik
#klucze
#wartosci
# k: v - element slownika

d = {"imie": "Jan", 
     "Nazwisko": "Kowalski", 
     "Telefon": 666777888
     }
print("Slownik", d, type(d))
print("Slownik klucze:", d.keys(), type(d.keys()))

print("Slownik values", d.values(),type(d.values()))

print("Slownik items", d.items(), type(d.items()))


# Wyjmujemy wartosc ze slownika bazujac na kluczu (klucz podany jako tekst bezposrednio lub prze zmienna)

example = 'imie'
print("Wyszukana wartosc:", d["imie"])
print("Wyszukana wartosc:", d[example])
