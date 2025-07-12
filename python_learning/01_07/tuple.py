krt = (1, 2, 3, 4, 5)
#krt[2] = 10

lst = list(krt)

print(lst)

lst[2] = 10

krt = tuple(lst)

print("Krotka to:", krt, "oraz typ:", type(krt))

print("Krotka to:{} oraz typ: {}".format(krt, type(krt)))
print("Krotka to:{0} oraz typ: {1}".format(krt, type(krt)))
print("Krotka to:{1} oraz typ: {1}".format(krt, type(krt))) #format

print(f"Krotka to:{krt} oraz typ: type{type(krt)}") # f-string