#numtoeng

x = input("Enter a number less than a million:  ")
z = (x % 1000)
y = (x / 1000)

def onesprefix(n):
    if n == 1:
        return " one"
    elif n == 2:
        return " two"
    elif n == 3:
        return " three"
    elif n == 4:
        return " four"
    elif n == 5:
        return " five"
    elif n == 6:
        return " six"
    elif n == 7:
        return " seven"
    elif n == 8:
        return " eight"
    elif n == 9:
        return " nine"
    else:
        return ""
def identifyteens(n):
    if n == 0:
        return " ten"
    elif n == 1:
        return " eleven"
    elif n == 2:
        return " twelve"
    elif n == 3:
        return " thirteen"
    elif n == 4:
        return " fourteen"
    elif n == 5:
        return " fifteen"
    elif n == 6:
        return " sixteen"
    elif n == 7:
        return " seventeen"
    elif n == 8:
        return " eighteen"
    elif n == 9:
        return " nineteen"
    else:
        return ""
def tensprefix(a):
    elif a == 2:
        return " twenty"
    elif a == 3:
        return " thirty"
    elif a == 4:
        return " forty"
    elif a == 5:
        return " fifty"
    elif a == 6:
        return " sixty"
    elif a == 7:
        return " seventy"
    elif a == 8:
        return " eighty"
    elif a == 9:
        return " ninety"
    else:
        return ""
def read1000(n):
    return read100(n) + read10(n) + read1(n)
def read100(n):
    if n / 100 >= 1:
        return (onesprefix(n/100) + "-hundred")
    else:
        return ""
def read10(n):
    if (n%100/10) >= 10:
        if tensprefix((n%100)/10) == "teen":
            return ""
        else:
            return tensprefix((n%100)/10)
    else:
        return ""
def read1(n):
    if read10(n) == "teen":
        return identifyteens(n%10)
    if read10(n) == "":
        return onesprefix(n%10)
    else:
        return "-"+ onesprefix(n%10)

def numtoeng():
    if y==0:
        return read1000(z)
    else:
        return read1000(y) + " thousand " + read1000(z)

print numtoeng()
def a():
    def b():
        print 5

