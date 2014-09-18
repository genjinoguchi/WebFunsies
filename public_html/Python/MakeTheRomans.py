#Roman Numerals up to 4000

n=input("Insert Number: ")

def readnums(n, one, five, ten):
    if n<4:
        return one*n
    elif n==4:
        return one+five
    elif n<9:
        return five + (one * (n-5))
    elif n<=10:
        return ((10-n)*one)+ten
    else:
        return ""
def numtorom(n):
    return readnums((n/1000), "M", "A", "B")+ readnums((n/100)%10, "C", "D", "M") + readnums((n/10)%10, "X", "L", "C") + readnums((n%10), "I", "V", "X")
print numtorom(n)
