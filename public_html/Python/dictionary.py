#Dictionaries

#use {}'s
#Each thing in a dictionary is distingt and all have a meaning(value)
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
    for each in m:
        ans[each] = freq(each,m)
    return ans
