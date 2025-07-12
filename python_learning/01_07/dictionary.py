slownik = {
    "key1": "value1",
    "key2":
    {
        "keyinside": "valuenside"
    }
    }
print(slownik)

print(slownik["key1"])

slownik["key1"] = 'newvalue1'

print(slownik["key1"])
del slownik["key2"] #usuniecie klucza
print(slownik)
#print(slownik["key2"])

#json - javascript object notation