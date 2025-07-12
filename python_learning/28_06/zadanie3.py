temp_fahr = float(input("Podaj temperaturę w Fahrenheita "))
kelvin_offset = 273.15
fahrenheit_to_celsius = 5/9
fahrenheit_constant = 32
temp_cel = (temp_fahr - fahrenheit_constant) * fahrenheit_to_celsius
print ("Temperatura w Celsjuszach:", temp_cel)
temp_kel = temp_cel + kelvin_offset
print ("Temperatura w Kelvinach:", temp_kel)


x = 5/9

print(f"{x:.2f}")
