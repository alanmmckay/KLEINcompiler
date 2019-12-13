import math 

def MOD(m,n):
    return m-(m/n)*n
def divisibleByParts(left, right):
    print("n/10=",left,"MOD(n,10)",right)
    return divisibleByDifference((left-right)*2)
def divisibleByDifference(diff):
    print("diff=", diff)
    if((diff == 7) or (diff == 0) or (diff == -7) or (diff == -14)):
        return True
    else:
        if(diff<14):
            return False
        else:
            main(diff)
def main(n):
    return divisibleByParts(n/10, MOD(n,10))

inputString = "Input value (input 0 to quit): "
x = input(inputString)
if(x != 0):
    while(True):
        x = int(x)
        if(x == 0):
            break
        print(main(x))
        x = input(inputString)
    

