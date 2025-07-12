class Calculator:
    def add(a,b):
        try:
            result = a + b
            return result
        except TypeError:
            return a + b
    
    def add(a,b):
        if type(a) == str or type(b) == str:
            return "cant add letter and number"
        else:
            result = a + b
            return result
    
    def add(a,b):
        if isinstance(a,str) or isinstance(b, str):
            return "cant add letter and number"
        else:
            result = a + b
            return result


    def subtract(a,b):
        return a - b

    def multiply(a,b):
        return a * b
    
    def divide(a,b):
        if b != 0:
            return a / b
        if b == 0:
             return "Zero devision error!"
        