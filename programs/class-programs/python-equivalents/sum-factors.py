def loopToN( n , current , sum ):
    if n == current:
        return n - sum
    else:
        return testAndLoop( n , current , sum )

def testAndLoop( n , current , sum ):
    if divides( current , n ):
        return printCurrentAndLoop( n , current , sum + current )
    else:
        return loopToN( n , current + 1 , sum )

def printCurrentAndLoop( n , current , sum ):
    print(current)
    return loopToN( n , current + 1 , sum )

def divides ( a , b ):
    return remainder( b , a ) == 0

def remainder( num , den ):
    if num < den:
        return num
    else:
        return remainder( num - den , den )

def main ( n ):
    return loopToN( n , 1 , 0 )
        
