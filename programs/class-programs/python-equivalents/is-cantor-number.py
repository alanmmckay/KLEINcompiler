def main ( n ):
    return has_no_2s(to_base3(n))
                     
def to_base3( n ):
    if n < 3:
        return n
    else:
         return 10 * to_base3(n / 3) + MOD(n, 3)


def has_no_2s( n ):
    if n < 10:
        return n < 2
    else:
        return has_no_2s(n / 10) and has_no_2s(MOD(n, 10))

def MOD( m , n ):
    return m - m/n * n

        
