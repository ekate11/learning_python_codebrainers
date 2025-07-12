warunek = 0
if warunek:
    print("Warunek to prawda")
elif warunek: 
    print("warunek1 to prawda")
else:
    print("Warunek to nieprawda, wybierz cos innego")

punkty = 72 
if punkty < 10:
    print("Mniej niz 10, nie zdales")
elif punkty < 20:
    print("Mniej niz 20, nie zdales")
elif punkty < 70:
    print("Mniej niz 70 nie zdales")
elif punkty >= 72:
    print("Zdales!")
    if True:
        print("Test")
        if False:
            print("Test")
else:
    print("Punkty poza skalą")

punkty = 60
# print("passed") if punkty >= 60 else print("not passed")
punkty = 40
# x = "Zdałeś" if punkty >= 50 and punkty < 100 else "Nie zdałeś"
x = "PASSED!" if punkty >= 50 and punkty < 100 else "FAILED"
print(x)
# Standardowa implementacja 
x = ""
if punkty >= 50 and punkty < 100:
    x = "PASSED"
else:
    x = "FAILED"