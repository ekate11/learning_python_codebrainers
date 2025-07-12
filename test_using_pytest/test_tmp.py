def test_dodawanie():
    x = 1
    y = 20
    expected = 21
    result = x + y
    print(expected == result)
    assert expected == result  
    #najwazniejsza linia if expected == result: print ("PASS") else: print ("Failed")

def test_dodawanie1():
    x = 1
    y = 20
    expected = 21
    result = x + y
    print(expected == result)
    assert expected == result  


#pytest -s (pokazuje prints)
#pytest -v (pokazuje oddzielnie uruchomione pliki)