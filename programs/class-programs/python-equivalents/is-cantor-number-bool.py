def main ( n ):
    return (n < 2) or ((2 < n) and main(n / 3) and main(MOD(n, 3)))

def MOD( m , n ):
    return m - m // n * n
