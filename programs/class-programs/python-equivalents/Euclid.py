def remainder ( a, b ):
    if a < b:
        return a
    else:
        return remainder( a - b , b)

def gcd( a , b ):
    if b == 0:
        return a
    else:
        return gcd( b , remainder ( a , b ))

def main ( a , b ):
    print (gcd ( a , b ))

