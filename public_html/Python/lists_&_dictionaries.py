
#Practice

import random
def makeList(size, minbound, maxbound):
    ans=[]
    while size>0:
        ans.append(random.randrange(minbound, maxbound))
        #list.append(1234567)
        size=size-1
    return ans
def makeList2(size, minbound, maxbound):
    ans=[]
    for each in range(size):
        ans.append(random.randrange(minbound, maxbound))
    return ans
    
def mean(L):
    if len(L)==0:
        return 0
    return float(sum(L)) / len(L)

def median(L):
    list.sort(L)
    return mean( [ L[len(L)/2] , L[(len(L)/2)+1] ])

def freq(num, L):
    ans=0
    for each in L:
        if each == num:
            ans=ans+1
    return ans

def makeset(L):
    list.sort(L)
    ans=[]
    for each in L:
        if each not in ans:
            ans= ans+[each]
    return ans

def histogram(L):
    for each in range(len(L)):
        print str(each) + (" "*(10-len(str(each)))) + "|   " + ("X " * freq(each, L))

def betterhist(L):
    for each in makeset(L):
        print str(each) + (" "*(10-len(str(each)))) + "|   " + ("X " * freq(each, L))

def localmodes(L):
    M = makeset(L)
    pos=1
    ans=[]
    while pos < (len(M)-1):
        if freq(M[pos], L) > freq(M[pos-1], L) and freq(M[pos], L) > freq(M[pos+1], L):
            ans.append(M(pos))
        pos=pos+1
    return ans

#n=input("enter size ")
#low, high = input("enter range ")
#list = makeList2(n, low, high)
#print list

#Dictionaries

#use {}'s
#Each thing in a dictionary is distinct and all have a meaning(value)
d = {} # <- Empty Dictionary.
d['cat'] = 3 # <- Assign new values
d['dog'] = 5
d['cat'] = 4 # <- Change value
d['dog'] = d['dog']*2

# d.keys() - gives back a list of all of the keys.]
# d.keys() = ['cat', 'dog'] (random order)
# d.values() - gives back a list of all of the values.]
# d.values() = ['3', '5'] (random order)

def freq(num, L):
    ans=0
    for each in L:
        if each == num:
            ans=ans+1
    return ans

def freqdic(L):
    ans={}
    m = makeset(L)
    m.sort()
    for each in m:
        ans[each] = freq(each,L)
    return ans

def modes(L):
    ans=[]
    fd=freqdic(L)
    mx = max(fd.values())
    for key in fd:
        if fd[key] == mx:
            ans.append(key)
    return ans

def reversedict(d):
    ans={}
    keys=makeset(d.values())
    for each in d.keys():
        if d[each] in ans.keys():
            ans[d[each]].append(each)
        else:
            ans[d[each]] = [each]
    return ans
        
#SparseArray is an array of mostly zeros.
# e.g. L1=[0, 0, 5, 0, 3, 0, 0, 1]
# sparseDict(L1)-> {2:5, 4:3, 7:1}

def sparseDict(L):
    ans={}
    pos=0
    while pos<len(L):
        if L[pos] == 0:
            pos=pos+1
        else:
            ans[pos]=L[pos]
            pos=pos+1
    return ans

def adddics(d1, d2):
    ans=d1
    for each in d2:
        if each in d1:
            ans[each]=d1[each]+d2[each]
        else:
            ans[each]=d2[each]
    return d1








