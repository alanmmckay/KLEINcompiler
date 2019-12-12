def main ( elementWanted):
    if elementWanted < 1 :
        return 0
    else:
        return addNext( 1 , elementWanted , 0 , 1 )

def addNext( currentElement, elementWanted , previousSum , currentSum):
    if elementWanted == currentElement:
        return currentSum
    else:
        return addNext ( currentElement + 1 , elementWanted , currentSum , previousSum + currentSum )
