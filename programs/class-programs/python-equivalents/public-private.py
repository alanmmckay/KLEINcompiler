def main ( publicKey , privateKey ):
    if publicKey == 0:
        return factor( 2147481647 , 2047483747 )
    else:
        return factor( publicKey , privateKey )

def factor( publicKey , privateKey ):
    return displayAndPrint( publicKey , privateKey , gcd( publicKey , privateKey) )

def displayAndPrint( publicKey , privateKey , commonFactor ):
    print( publicKey  // commonFactor )
    print( privateKey // commonFactor )
    return commonFactor

def gcd( a , b ):
    if b == 0:
        return a
    else:
        return gcd( b , remainder( a , b ) )

def remainder( a , b ):
    if a < b:
        return a
    else:
        return remainder( a - b , b )
    
