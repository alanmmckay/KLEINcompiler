def main ( x ):
    return horner ( x , 3 , 0 )

def horner( x , n , value ):
    if n < 0:
        return value
    else:
        return horner( x , n - 1 , (value * x) + coefficient(n) )

def coefficient( i ):
    if i < 1:
        return 9
    elif i < 2:
        return 2
    elif i < 3:
        return -4
    else:
        return 1
