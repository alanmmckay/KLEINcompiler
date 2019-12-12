#MOD is undefined

def main( x ):
    return is_tanton_pal_bin(binary_for(x))

def is_tanton_pal_bin( x ):
    if is_palindrome( x ):
        return True
    else:
        return is_tanton_pal_bin( add_boolean( x , reverse( x )) )

def binary_for( n ):
    if n < 2:
        return n
    else:
        return 10 * binary_for( n // 2 ) + MOD( n , 2 )

def decimal_for( n ):
    if n < 10:
        return n
    else:
        return 2 * decimal_for( n // 10) + MOD( n , 10 )

def add_boolean( m , n ):
    return  binary_for( decimal_for( m ) + decimal_for( n ))

def is_palindrome( n ):
    return n == reverse ( n )

def reverse( n ):
    return reverseL( n , 0 )

def reverseL( n , nR ):
    if n == 0:
        return nR
    else:
        return reverseL( n // 10 , 10 * nR + MOD ( n , 10 ))
    
