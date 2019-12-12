def MOD(m,n):
    return(m%n)

def multWithAccum(m,n,accum):
    if n==0:
        return(accum)
    elif MOD(n,2)==1:
        return(multWithAccum(m*2,n//2,accum+m))
    else:
        return(multWithAccum(m*2,n//2,accum))

def mult(m,n):
    return(multWithAccum(m,n,0))

def main(m,n):
    print(m)
    return(mult(m,n))

answer=main(9,6)
print("The value is : ",answer)
