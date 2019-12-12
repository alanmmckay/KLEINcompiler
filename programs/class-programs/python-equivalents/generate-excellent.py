# bad if

def MOD( m , n ):
    return  m - n *( m// n )

def EXP( m , n ):
    if n == 0:
        return 1
    else:
        return m * EXP( m , n-1 )

def ODD( n ):
    if 0 < n:
        return (2 * ( n // 2 )) < n
    else:
        return ODD( -n )

def LE( p , q ):
    return ( p < q ) or ( p == q )

def SQRT( n ):
    return SQRTSEARCH( n , 0 , n )

def SQRTSEARCH( n , low , high ):
    if LE( high, low + 1 ):
        if LE( n - (low * low) or (high * high) - n ):
            return low
        else:
            return high
    else:
        return  SQRTSPLIT( n, low, high, (low + high)// 2 )

def SQRTSPLIT( n , low , high , mid ):
    if LE( mid * mid , n ):
        return SQRTSEARCH( n, mid, high )
    else:
        return SQRTSEARCH( n, low, mid )

def EVEN( n ):
    return  n == (2 * (n//2))

def ISROOT( r , n ):
    return  n == r*r

def length( n ):
    if n < 10:
        return 1
    else:
        return 1 + length( n // 10 )

def a( n ):
    return n // EXP(10, length(n)// 2 )

def excellentDiff( a , b ):
    return b * b - a * a

def isExcellentSwitch( n , length):
    if ODD(length):
        return False
    else:
        return n == excellentDiff(a(n), b(n))

def isExcellent( n ):
    return isExcellentSwitch( n , length(n) )

def printCandidateAndContinue( a , n , upper , candidate ):
    print(candidate)
    return aLoop( a + 1 , n , upper )

def aLoop3( a , n , upper , det , root , candidate):
    if ISROOT(root, det) and EVEN(root + 1) and isExcellent(candidate):
        return printCandidateAndContinue(a, n, upper, candidate)
    else:
        return aLoop(a+1, n, upper)

def aLoop2( a , n , upper , det , root ):
    return aLoop3(a , n , upper , det , root , a * EXP(10, n) + ((root + 1) // 2))

def aLoop1( a , n , upper , det ):
    return aLoop2(a, n, upper, det, SQRT(det))

def aLoop( a , n , upper ):
    if a < upper:
        return aLoop1(a , n , upper , 4*EXP(a , 2) + 4*EXP(10 , n)* a + 1 )
    else:
        return True
    
def createLoop( a , n ):
    return aLoop( a , n , 10 * a )

def main ( length):
    return createLoop(EXP(10 , length // 2 - 1 ), length//2 )




