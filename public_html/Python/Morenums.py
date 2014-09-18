#Random Phone Numbers

import random

def pnums():
    total=10
    num=''
    while total>0:
        if total==1:
            num = str(random.randrange(2, 10)) + num
        else:
            num = str(random.randrange(0, 10)) + num
            if total == 7 or total == 4:
                num = '-' + num
        total=total-1
    print num
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()
pnums()

def shufflehelp(n):
    ans=''
    for each in str(n):
        if random.randrange(0, 2) == 0:
            ans=ans+each
        else:
            ans=each+ans
    return ans
def shuffle(n):
    print shufflehelp(shufflehelp(shufflehelp(shufflehelp(n))))

def shuffle2(n):
    ans=''
    for each in str(n):
        rand= (random.randrange(0, len(str(n))))
        ans=str(n)[:rand] + each + str(n)[rand: ]
    print ans

def shuffle3(n):
    ans=''
    nString=str(n)
    while len(nString)>0:
        pos = random.randrange(0,len(nString))
        ans = nString(pos)+ ans
        nString = nString[:pos] + nString[pos+1:]

shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)
shuffle2(105)



