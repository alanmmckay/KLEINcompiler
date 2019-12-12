def main( n ):
    return sieveAt( 2 , n )

def sieveAt( current , max ):
    if max < current:
        return True
    else:
        return doSieveAt( current , max )

def doSieveAt( current , max ):
    if isPrime(current):
            print (current)
    else:
        print ("0")
    return sieveAt(current+1 , max )

def isPrime( n ):
    return  not hasDivisorFrom(2, n)

def hasDivisorFrom( i , n ):
    if i < n:
        return divides(i, n) or hasDivisorFrom(i+1, n)
    else:
        return False

def divides( a , b ):
    return rem( b , a ) == 0

def rem( num , den ):
    if num < den:
        return num
    else:
        return rem( num - den , den )
        
