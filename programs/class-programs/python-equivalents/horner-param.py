def main( coeff3, coeff2 , coeff1 , coeff0 , x ):
    return horner( x, 3, 0, coeff3, coeff2, coeff1, coeff0 )

def horner( x , n , value , coeff3 , coeff2 , coeff1 , coeff0 ):
    if n < 0:
        return value
    else:
        return horner( x , n - 1 , (value * x) + coefficient(n, coeff3, coeff2, coeff1, coeff0),
               coeff3, coeff2, coeff1, coeff0 )
    
def coefficient( i , coeff3 , coeff2 , coeff1 , coeff0 ):
    if i < 1:
        return coeff0
    elif i < 2:
        return coeff1
    elif i < 3:
        return coeff2
    else:
        return coeff3
    
