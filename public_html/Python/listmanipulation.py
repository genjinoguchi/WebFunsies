#List Manipulation

def odds(n):
    if n==1:
        return [1]
    elif n%2==0:
        return Nodds(n-1)
    else:
        return Nodds(n-2)+[n]
def odds2(n):
    return range(1, n, 2)

def Noddshelp(a,b):
    if b==1:
        return [a]
    else:
        return [a]+Noddshelp(a+2,b-1)
def Nodds(n):
    return Noddshelp(1,n)
def Nodds2(n):
    return range(1, 2n, 2)
