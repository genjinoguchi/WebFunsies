def removeA(s):
    length=0
    total=""
    while length <= (len(s)-1):
        if s[length] == "a":
            length=length+1
        else:
            total=total+s[length]
            length=length+1
    return total


def removeaA(s):
    final=''
    for each in s:
        if each not in 'aA':
            final=final+each
    return final

def reverse(s):
    final=''
    for each in s:
        final=each+final
    return final

def isPalindrome(word):
    return word == reverse(word)

def collect(s, letset):
    final=''
    for each in s:
        if each in letset:
            final=final+each
    return final
def collectA(s):
    return collect(s, "aA")
def collectvowels(s):
    return collect(s, "aAeEiIoOuU")
def isvowel(s):
    return s in 'aAeEiIoOuU'
def piglatin(s):
    for each in s:
        if isvowel(s[0]):
            return s + 'way'
        elif isvowel(each):
            final=s[s.find(each),]+s[s.find(each) - 1]+'ay'
            return final                
#x=raw_input("Enter A Word:  ")
#print "Palindrome?", isPalindrome(x)
#print "Palindrome:", reverse(x)
#print "Vowels:", collectvowels(x)
