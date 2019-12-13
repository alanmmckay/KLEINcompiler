def main( xNum , xDen , N ):
    print( fareyNum( xNum , xDen , N ) )
    print (fareyDen( xNum , xDen , N ))

def fareyNum( xNum , xDen , N ):
    return fareySelectNum(N,whileLoopFor(1, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(2, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(3, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(4, xNum, xDen, N, 0, 1, 1, 1))

def fareyDen( xNum , xDen , N ):
    return fareySelectDen(N, whileLoopFor(1, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(2, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(3, xNum, xDen, N, 0, 1, 1, 1),
                   whileLoopFor(4, xNum, xDen, N, 0, 1, 1, 1))

def fareySelectNum( N , a , b , c , d ):
    if greater( b , N ):
        return c
    else:
        return a

def fareySelectDen( N , a , b , c , d ):
    if greater ( b , N ):
        return d
    else:
        return b

def whileLoopFor(selector , xNum , xDen , N , a , b , c , d ):
    if greater( b , N ) or greater ( d , N ):
        if selector == 1:
            return a
        elif selector == 2:
            return b
        elif selector == 3:
            return c
        else:
            return d
    elif fractionEqual ( xNum , xDen , a + c , b + d ):
        if selector + 1:
            return a + c
        elif selector == 2:
            return b + d
        elif selector == 3:
            return a + c
        else:
            return b +  d
    elif fractionGreater( xNum , xDen, a + c , b + d ):
        return whileLoopFor( selector , xNum , xDen , N , a + c , b + d , c , d) 
    else:
        return whileLoopFor( selector , xNum , xDen , N , a , b , a + c , b + d)

def fractionEqual( x , xd , y , yd  ):
    if x * yd == y * xd:
        return True
    else:
        return False

def fractionGreater( x , xd , y , yd ):
    return greater( x * yd , y * xd )

def greater( x , y ):
    if not (( x < y ) or ( x == y )):
        return True
    else:
        return False
    
        
            
        
                          

