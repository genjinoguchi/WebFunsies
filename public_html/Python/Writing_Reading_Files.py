#Writing and Reading to Files

#   __myprogram.py__        writestuff       ____data.txt__
#   |               |   File Stream         |             |
#   |   Source      | ----------->>>>>>>>>> |             |
#   |   Code        |   Only one            |             |
#   |_______________|   direction           |_____________|

#fileHandle = open("data.txt","w")
#fileHandle.write("cat")
#fileHandle.write("dog")
#fileHandle.close()

#   You can only send a string, so you have to convert non-strings
#   before sending.

#fileHandle = open("data.txt","w")  #w for write
#fileHandle.write("cat/n")  #sends a cat and a new line.
#fileHandle.write("dog/n")
#fileHandle.close()

import random
def randoms(n, filename):
    move = open(filename, "w")
    while n > 0:
        move.write(str(random.randrange(0, 101))+"\n")
        n-=1
    move.close()

#   __myprogram.py__        readstuff        ____data.txt__
#   |               |   File Stream         |             |
#   |   Source      | <<<<<<<<<------------ |             |
#   |   Code        |   Only one            |             |
#   |_______________|   direction           |_____________|

#fileHandle=open("data.txt","r")
#L = fileHandle.read()
#L -> "33/n25/n"
#L=L.split() ->>>> returns [33, 25]
#   The file will be created at the same location
#   as the place that your .py file is located.

def sumFile(filename):
    fil = open(filename, "r")
    lis=fil.read()
    lis=lis.split()
    ans=0
    lis = map(int, lis)
    fil.close()
    return sum(lis)

#   map(operator, list)-> operator is applied to each item in the list.

def evenodds(filename):
    datafil = open('data.txt', 'r')
    oddfil = open('odd.txt', 'w')
    evenfil = open('even.txt', 'w')
    datalis = map(int, datafil.read().split())
    oddlis = ""
    evenlis = ""
    for each in datalis:
        if each % 2 == 1:
            oddlis+=str(each) + "\n"
        else:
            evenlis+=str(each) + "\n"
    oddfil.write(oddlis)
    evenfil.write(evenlis)
    oddfil.close()
    evenfil.close()
    datafil.close()

def charcount(filename):
    f = open(filename, "r")
    print "characters:  ", len(f.read())
    f.close()

def charcount2(filename):
    f = open(filename, "r")
    chars=""
    for each in f:
        chars+=each
    print "characters:  ", len(chars)
    f.close()

def wordcount(filename):
    f = open(filename, "r")
    print "words:   ", len(f.read().split())
    f.close()

def linecount(filename):
    f = open(filename, "r")
    lines=0
    while f.readline() != "":
        lines+=1
    f.close()
    print "lines:  ", lines

def linecount2(filename):
    f=open(filename, "r")
    lines=0
    for line in f:
        lines+=1
    f.close()
    print "lines:  ", lines

def printfreqs(filename):
    f=open(filename, "r")
    list=f.read().split()
    dic={}
    length=max(map(len, list))+5
    for each in list:
        if each in dic:
            dic[each]+=1
        else:
            dic[each]=1
    write=open("analysis1.txt", "w")
    for each in dic:
         write.write(str(each)+":"+(length-len(each))*" "+str(dic[each])+"\n")
    f.close()
    write.close()

#   file.readline() ->  "This is a line./n"
#   file.readline() ->  "This is another line./n"
#   file.readline() ->  "This is the last line./n"
#   file.readline() ->  ""

#   str.strip() -> Removes leading and ending spaces
#   str.strip("string") -> removes strings from lead and end

def removepunc(filename):
    f=open(filename, "r")
    list=""
    for each in f:
        list+=each.strip("\n.,;:?!")+" "
    return list
        








linecount2("text.text")
wordcount("text.text")
charcount2("text.text")
printfreqs("text.text")
print removepunc("text.text")

#n = input("how many numbers  ")
#filename = 'data.txt'
#randoms(n, filename)
#print 'look in:  ', filename
#print 'evens:    even.txt'
#print 'odds:     odd.txt'
#print 'sum:      ', sumFile(filename)
#evenodds(filename)
