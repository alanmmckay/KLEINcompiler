def MOD( m , n ):
    return m - m // n * n

def divides( x , n ):
    return MOD ( n , x ) == 0

def count( x , n ):
    if n < 10:
        if x == n:
            return 1
        else:
            return 0
    else:
        if x == MOD( n , 10 ):
            return 1 + count(x, n // 10)
        else:
            return count(x, n // 10)

def to_binary( n ):
    if n == 0:
        return 0
    else:
        return 10 * to_binary(n // 2) + MOD(n , 2)

def apply_definition( binary_n , n ):
    return divides (count(1, binary_n), n) and divides(count(0, binary_n), n)

def main( n ):
    return apply_definition(to_binary(n) , n )
