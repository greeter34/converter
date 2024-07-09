def f2c(a): #fahrenheit to celsius conversion
    result = (a - 32) * (5 / 9)
    return result

def c2f(a): #celsius to fahrenheit conversion
    result = (a * (9 / 5)) + 32 
    return result

def c2k(a): #celsius to kelvin conversion
    result = a + 273.15
    return result

def k2c(a): #kelvin to celsius conversion
    result = a - 273.15
    return result

def f2r(a): #fahrenheit to rankine conversion
    result = a + 459.67
    return result

def r2f(a): #rankine to fahrenheit conversion
    result = a - 459.67
    return result

