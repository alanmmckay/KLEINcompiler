def MOD( m, n):
    if m < n: 
        return m
    else:
        MOD(m-n, n)
        
def main( m, n):
    print(m / n)
    return MOD(m,n)
