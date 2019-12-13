import sys  

def printAndDivide ( a, b, n ):
    print( 10 * a // b)
    return main ( MOD(a*10, b), b, n-1)

def MOD ( m, n):
    return m - m//n * n

sys.argv = ['printAndDivide', '1' , '2', '3' ]

def main ( a, b, n ):
    if n == 0 :
        return a
    else:
        return printAndDivide( a, b, n )

print( main( int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))) 
