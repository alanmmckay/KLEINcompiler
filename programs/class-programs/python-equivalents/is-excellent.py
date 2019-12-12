def MOD( m , n ):
    return m - n * (m//n)

def EXP( m , n ):
    if n == 0:
        return 1
    else:
        return m * EXP( m , n-1 )

def ODD( n ):
    if 0 < n:
        return ( 2 * (n//2) ) < n
    else:
        return ODD( -n )

def length( n ):
    if n < 10:
        return 1
    else:
        return 1 + length( n // 10)

def a( n ):
    return n // EXP( 10, length(n)//2 )

def b( n ):
    return MOD( n, EXP(10, length(n)//2) )

def excellentDiff( a , b ):
    return b * b - a * a

def isExcellentSwitch( n , length ):
    if ODD( length ):
        return False
    else:
        return n == excellentDiff( a(n), b(n) )

def isExcellent( n ):
    return isExcellentSwitch( n, length(n) )

def main( n ):
    return isExcellent( n )
    


    
