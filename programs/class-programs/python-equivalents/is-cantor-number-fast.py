def main( n ):
    if n < 3:
        return n < 2
    else:
        return main( n // 3) and main(MOD(n , 3))

def MOD( m , n ):
    return m - m // n * n
