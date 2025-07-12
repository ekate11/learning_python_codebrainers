int_value = 5
var1 = 2
var2 = 5
var3 = var1 + var2
print(var3)
print(type(var3))
var4 = float(var1) + float(var2)
print(var4)
print(type(var4))
float_value = 4.70
complex_value = 1 + 2j


print(int_value)
print(float_value)
print(complex_value)

char1 = "text"
print("Char1 typ", type(char1))

print ("Float type:", type(float_value))
print ("Complex type:", type(complex_value))

print(f"{var4:.10f}") # Wyświetla var4 z dwoma miejscami po przecinku

# Konwersja liczby zmiennoprzecinkowej na calkowita
f1 = 5.6
f2 = 5.5
f3 = 5.4
i1 = int(f1)
print("i1", i1)
i2 = int(f2)
print("i2", i2)
i3 = int(f3)
print("i3", i3)

print ("Zaokraglenie:",round(f1))
print ("Zaokraglenie:",round(f2))
print ("Zaokraglenie:",round(f3))