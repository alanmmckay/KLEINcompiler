def MOD( m , n ):
    return m - n*( m // n )

def reverse(n ):
    return reverseL( n , 0 )

def reverseL( n , nR ):
    if n == 0:
        return nR
    else:
        return reverseL( n // 10 , 10 * nR + MOD(n, 10) )

def isPalindrome( n ):
    return 0 == ( n - reverse(n) )

def main( number ):
    print(number)
    print(reverse(number))
    return isPalindrome(number)

        


