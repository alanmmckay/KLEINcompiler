def main( testArgument):
    print(SQRT(testArgument) )
    return ODD( testArgument )

def MAXINT():
    return  2147483647

def MININT():
    return -2147483647 - 1

def LT ( p , q ):
    return p < q

def EQ( p , q ):
    return p == q

def NE( p , q ):
    return not EQ( p , q )

def LE( p , q ):
    return LT( p , q ) or EQ( p , q )

def GE( p , q ):
    return not LT( p , q )

def GT( p , q ):
    return not LE( p , q )

def OR( p , q ):
    return p or q

def AND( p , q ):
    if p:
        return q
    else:
        False

def PLUS( p , q ):
    return p + q

def MINUS( p , q ):
    return p - q

def TIMES( p , q ):
    return p * q

def DIV( p , q ):
    return p // q

def NEG( n ):
    return -n

def ABS( n ):
    if 0 < n:
        return n
    else:
        return NEG(n)

def MOD( m , n ):
    return  m - m/n * n

def EXP( m , n ):
    if n == 0:
        return 1
    else:
        return m * EXP( m , n-1 )

def ODD( n ):
    if LE( 0 , n ):
        return GT( n , DIV( n , 2 ) + DIV(NEG(n) , 2 ) )


def SQRT( n ):
    return SQRTSEARCH( n , 0 , n )

def SQRTSEARCH( n , low , high ):
    if LE( high , low + 1 ):
        if LE( n - TIMES(low,low), TIMES(high,high) - n ):
            return low
        else:
            return high
    else:
        return SQRTSPLIT( n, low, high, PLUS(low, high)// 2 )

def SQRTSPLIT( n , low , high , mid ):
    if LE( mid * mid , n ):
        return SQRTSEARCH( n , mid , high )
    else:
        return SQRTSEARCH( n , low , mid )
            

