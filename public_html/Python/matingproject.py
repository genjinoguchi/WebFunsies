#    Dictionary Project D:
#    email:  rick.platek@stuycs.org

men = ['abe', 'greg', 'dave']
women = ['sally', 'linda', 'cindy']

#  Create a dictionary for men's preferences

menPref={}
menPref['abe']  = {1:'linda', 2:'cindy', 3:'sally'}
menPref['greg'] = {1:'linda', 2:'cindy', 3:'sally'}
menPref['dave'] = {1:'sally', 2:'linda', 3:'cindy'}

womenPref={}
womenPref['sally'] = {1:'abe', 2:'greg', 3:'dave'}
womenPref['linda'] = {1:'greg', 2:'abe', 3:'dave'}
womenPref['cindy'] = {1:'dave', 2:'abe', 3:'greg'}

#               'abe'->'sally'
#               'greg'->'linda'
#               'dave'->'cindy'

def makeset(L):
    list.sort(L)
    ans=[]
    for each in L:
        if each not in ans:
            ans= ans+[each]
    return ans
    
def reversedict(d):
    ans={}
    keys=makeset(d.values())
    for each in d.keys():
        if d[each] in ans.keys():
            ans+=each
        else:
            ans[d[each]] = each
    return ans


final={}
def generatemarriages(manpref, womanpref):
    

def check(asker, choice):
    L=[choice]
    while L[-1] != asker:
        if victim in women:
            L.append(womenPref[L[-1]][1])
        else:
            L.append(menPref[L[-1]][1])
    final[asker]=L[-2]
    final[L[-2]=asker
    
def checkman(







    


       
