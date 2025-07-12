a = 10
b = 20
c = 0

print(a > b and c < b)
print(a > b or c < b)

print (not a)
print(not c)

a = 10
b = 20 
c = 0 
print("Wynik dzialania", a > b and c < b)
# false and true
print("Wynik dzialania", a > b or c < b)
# false or true
print("Wynik dzialania", not a)
# W przypadku gdy zmienna ma wartosc 0, [], {}, () to domyslnie
# jest to false 
# W przypadku gdy zmienna jest niezerowa to wtedy mamy wartosc true 
print("Wynik dzialania ptrojny warunek" \
      "to:", a > b and b > c or a > c)
            # false and true 
            # false or true            wynik finalny = true

print("Wynik dzialania ptrojny warunek" \
      "to:",a > b and (b > c or a > c)) #WYNIK FALSE

 #            FALSE    AND  (TRUE OR TRUE)