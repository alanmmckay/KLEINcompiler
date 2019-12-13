def main ( a , b , n ):
    if n == 0:
        return a
    else:
        printAndDivide( a , b, n )

def printAndDivide( a , b , n ):
    print(( 10 * a ) // b )
    return main (MOD(a*10, b), b, n-1)

def MOD( m , n ):
    return m - m // n * n
