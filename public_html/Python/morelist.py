#List

def divlist(n):
    ans=[]
    for each in range(1, n+1):
        if n%each==0:
            ans=ans+[each]
    return ans

def hailstone(n):
    ans=[n]
    while n != 1:
        if n%2==1:
            n=3*n+1
        else:
            n=n/2
        ans=ans+[n]
    return ans

def fib(n):
    ans=[0, 1, 1]
    while len(ans)<n:
        ans=ans + [ans[-1]+ans[-2]]
    return ans
