
#Precondition- n is an integer, n>=0
#While loops!

def factorial(n):
    final=1
    while n > 0:
        final=final*n
        n=n-1
    return final
def numdigits(n):
    final=1
    while n/10>0:
        final=final+1
        n=n/10
    return final
def numdigits2(n):
    return len(`n`)
def sumdigits(n):
    final=0
    while n>0:
        final=final+(n%10)
        n=n/10
    return final
def maxdigit(n):
    mx=n%10
    while n/10>0:
        n=n/10
        mx = max(mx, n%10)
    return mx
def commas(n):
    ans=""
    while n/1000>0:
        ans=","+`n%1000`+ans
        n=n/1000
    print `n`+ans

def even(n):
    return n%2 == 0
def odd(n):
    return not even(n)
def oddDigits(n):
    ans=''
    for nums in str(n):
        if odd(int(nums)):
            ans = ans+nums
    if ans=='':
        ans=-1
    return int(ans)
def odddig2(n):
    ans=''
    while n>0:
        if odd(n%10):
            ans=str(n%10)+ans
        n=n/10
    if ans=='':
        ans=-1
    return int(ans)
def odddig3help(n):
    if n/10==0 and even(n):
        return ""
    elif odd(n):
        return odddig3help(n/10) + str(n%10)
    else:
        return odddig3help(n/10)
def odddig3(n):
    if odddig3help(n) == '':
        return -1
    else:
        return int(odddig3help(n))
def reverse(n):
    ans=''
    for num in str(n):
        ans=num+ans
    return int(ans)
import random
def randomDig(n):
    return int(str(n)[random.randint(0, len(str(n)))])
def randomPhoneNumber():
    ans=''
    dig=7
    while dig > 0:
        if dig==3 or dig==6:
            ans=ans+str(random.randrange(0, 10))+"-"
        else:
            ans=ans+str(random.randrange(0, 10))
    return ans

n=input("enter ")
print n, "!= ", factorial(n)
print "Digits: ", numdigits2(n)
print "Sum of Digits: ", sumdigits(n)
print "Greatest Digit: ", maxdigit(n)
