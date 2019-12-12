import math 

def main ( n ):
    return divisibleByParts ( n // 10 , MOD (n, 10 ))

def divisibleByParts ( left , right ):
    return divisibleByDifference ( left - right * 2)

def divisibleByDifference ( diff ):
    if ((diff == 7) or (diff == 0) or (diff == -7) or (diff == -14)):
        return True
    else:
        if diff < 14:
            return False
        else:
            return main( diff )

def MOD (m , n ):
    return  m - m  //  n * n 




    
