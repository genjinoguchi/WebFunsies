import math

def f(x):
    return x + 2.
def g(x):
    return 2. * x
def h(x):
    return f( g(x) )
def myabs(x):
    if x >= 0:
        return x
    else:
        return -x
def mymax(x, y):
#    x=input("First Number:  ")
#   y=input("Second Number:  ")
    if x>y:
        return x
    elif x<y:
        return y
    else:
        print "They are equal"
def circlearea():
#    r=input("Circle Radius")
    return ((22. / 7.) * r**2)

def mymax3(x, y, ):
#    x=input("First Number:  ")
#    y=input("Second Number:  ")
#    z=input("Third Number:  ")
    if x >= y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else: return z

def mymaxagain(x, y, z):
    return (mymax(mymax(x, y), z))
def annulusarea():
    r1=input("Larger Annulus Radius:  ")
    r2=input("Smaller Annulus Radius:  ")
    return circlearea(r1)-circlearea(r2)

def onesdigit(n):
    return (n % 10)
def last2digs(n):
    return (n % 100)
def removdig(n):
    return (n / 10)


def functions():
    n = input ("Enter a number:  ")
    print "f(n) = ", f(n)
    print "g(n) = ", g(n)
    print "h(n) = ", h(n)
    print "Absolute Value: ", myabs(n)

def a():
    print 3
