def main( n ):
    loopToN ( n , 1)

def loopToN( n , current ):
    if n == current:
        return n
    else:
        return testAndLoop( n , current )

def testAndLoop( n , current ):
    if divides( current , n ):
        return printAndLoop( n , current)
    else:
        return loopToN( n , current + 1 )

def printAndLoop( n , current ):
    print(current)
    return loopToN( n , current + 1 )

def divides( a , b ):
    return remainder ( b , a ) == 0

def remainder( num , den ):
    if num < den:
        return num
    else:
        return remainder( num - den , den )
    
