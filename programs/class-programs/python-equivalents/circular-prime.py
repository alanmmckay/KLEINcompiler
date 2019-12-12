# maximum recursion depth exceeded in comparison


import math

def main(x):
    return circularPrimesTo(x)

def circularPrimesTo(x):
    return circularPrimesToHelper(x+1,2,0)

def circularPrimesToHelper(top,x,count):
    if x<top:
        if isCircularPrime(x):
            return circularPrimesToHelper(top,x+1,count+1)
        else:
            return circularPrimesToHelper(top,x+1,count)
    else:
        return count

def isCircularPrime(x):
    if isCircularPrimeHelper(x,math.log10(x)+1):
        return report(x)
    else:
        return False

def isCircularPrimeHelper(x,turns):
    if turns==0:
        return True
    else:
        return isPrime(x) and isCircularPrimeHelper(rotate(x),turns-1)

def report(x):
    print(x)
    return True

def rotate(x):
    return x/10+((x%10)*(10**math.log10(x)))

def isPrime(n):
    return not hasDivisorFrom(2,n)

def hasDivisorFrom(i,n):
    if i<n:
        return divides(i,n) or hasDivisorFrom(i+1,n)
    else:
        return False

def divides(a,b):
    return (b%a==0)



