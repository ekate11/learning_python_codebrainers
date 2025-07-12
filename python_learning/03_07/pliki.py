file_example_txt = open("file_example.txt", "w")
file_example_txt.write("Jestem na kursie w Codebrainers lipiec 2025\n")
file_example_txt.writelines("Dopisane bez menagera kontekstu\n")
file_example_txt.close()
# wykorzystanie managera kontekstu - automatycznie zamyka plik
with open("file_example.txt", "a") as file_example_txt:
    file_example_txt.writelines("Dopisujemy do pliku!\n")
    file_example_txt.writelines("ERROR\n")
    file_example_txt.writelines("ISSUE\n")
    file_example_txt.writelines("WARNING\n")
# wykorzystanie managera kontekstu - automatycznie zamyka plik - czytamy caly plik w calosci, wyswietlamy linia po linijce 
with open("file_example.txt", "r") as file_example_txt:
    print(file_example_txt.read())
# przeczytaj pierwsza linijke lub kolejna 
with open("file_example.txt", "r") as file_example_txt:
    print(file_example_txt.readline())
    print(file_example_txt.readline())
# przeczytaj pierwsza linijke lub kolejna 
with open("file_example.txt", "r") as file_example_txt:
    print(file_example_txt.readlines())

# przeczytaj pierwsza linijke lub kolejna 
with open("file_example.txt", "r") as file_example_txt:
    lines = file_example_txt.readlines()
    iter = 1
    for line in lines:
        if "ERROR" in line:
            print("Bład w lini numer:", iter)
        iter += 1

try:
    with open ("niejestniejcy_plik.txt", "r") as non_existing:
        non_existing.read()
except FileNotFoundError as e:
    print("ERROR", e)

nazwa_pliku = input(r"Podaj nazwe pliku:")

