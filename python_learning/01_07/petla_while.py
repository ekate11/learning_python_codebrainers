i = 0
while(True):
    print("Przebieg petli:", i)
    i +=1
    if i == 10:
        break


while(True):
    prompt = input("Wpisz polecenie")
    if prompt == "a":
        print("Wybrales odpowiedz a")
    elif prompt == 'b':
        print("Wybrales odpowiedz b")
    elif prompt == 'k':
        print("koniec programu")
        break #continue #break 
    else:
        print("Wybrales bledna odpowiedz")




