def ABS( n ):
    if n < 0:
        return -n
    else:
        return n

def f( x , n ):
    return x * x - n

def df( x ):
    return 2 * x

def newtonAux( guess , previous, epsilon , n ):
    if epsilon < ABS(previous - guess):
        return newtonAux( guess - f(guess,n)/df(guess), guess, epsilon, n )
    else:
        return guess

def newton( guess , epsilon , n ):
    return newtonAux( guess - f (guess,n )// df(guess), guess, epsilon, n )

def main( n , epsilon):
    return newton( n//2, epsilon, n )
