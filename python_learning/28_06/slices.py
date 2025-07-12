words = "Jestem na kursie tester oprogramowania w Codebrainers"
words_lenght = len(words)   # Przyjmuje sekwencje 
print("dlugosc napisu:", words_lenght)
# W pythonie indeksowanie zaczyna sie od 0 
print(words[0]) # pierwszy znak  
print(words[52]) # ostatni znak dlugosc napisu - 1
print(words[-1]) # ostatni znak 
print(words[-2]) # przedostatni znak
print(words[0:6]) # od 0 do 6 (nie wliczajac 6)
print(words[2:6]) 
print(words[10:20])
print(words[15:]) # od 15 do konca 
print(words[0:-1:2])
start = 0 
end = 30
step = 2
print(words[start:end:step])


#ciagi znakow niezmienne (imutable)
new_words = "tekst"
#new_words[0]="T". #nie dziala

new_character = "T"
new_words = new_character + new_words[1:]
print(new_words)
