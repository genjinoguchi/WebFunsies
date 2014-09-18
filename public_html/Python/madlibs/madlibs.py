#!/usr/bin/python
print 'Content-Type: text/html'
print

#   MADLIBS

import random

def getText(filename):
    read = open(filename, 'r')
    words=read.read()
    read.close()
    return words

def replaceall(words, newset, old, change, color):
    length=len(old)
    if words.find(old)==-1:
        return words
    x=randompop(newset)
    while words.find(old) >=0:
        start=words.find(old)
        if change==False:
            words=words[:start] + "<font color=" + color + ">" + randompop(newset) + "</font>" + words[start+length:]
        else:
            words=words[:start] + "<font color=" + color + ">" + x + "</font>" + words[start+length:]
    return words

def randompop(words):
        return words.pop(random.randrange(len(words)))

def madlibs(wordfile, nounfile, verbfile, adjfile, adverbfile, namefile):
    words=getText(wordfile)
    nouns=getText(nounfile).split()
    verbs=getText(verbfile).split()
    adverbs=getText(adverbfile).split()
    names=getText(namefile).split()
    adjectives=getText(adjfile).split()
    words = replaceall(words, adverbs, "ADVERB1", True, '"green"')
    words = replaceall(words, adverbs, "ADVERB2", True, '"green"')
    words = replaceall(words, adverbs, "ADVERB3", True, '"green"')
    words = replaceall(words, nouns, "NOUN1", True, '"red"')
    words = replaceall(words, nouns, "NOUN2", True, '"red"')
    words = replaceall(words, nouns, "NOUN3", True, '"red"')
    words = replaceall(words, verbs, "VERB1", True, '"blue"')
    words = replaceall(words, verbs, "VERB2", True, '"blue"')
    words = replaceall(words, verbs, "VERB3", True, '"blue"')
    words = replaceall(words, adjectives, "ADJECTIVE1", True, '"pink"')
    words = replaceall(words, adjectives, "ADJECTIVE2", True, '"pink"')
    words = replaceall(words, adjectives, "ADJECTIVE2", True, '"pink"')
    words = replaceall(words, names, "NAME1", True, '"yellow"')
    words = replaceall(words, names, "NAME2", True, '"yellow"')
    words = replaceall(words, names, "NAME3", True, '"yellow"')
    words = replaceall(words, nouns, "NOUN", False, '"red"')
    words = replaceall(words, adverbs, "ADVERB", False, '"green"')
    words = replaceall(words, verbs, "VERB", False, '"blue"')
    words = replaceall(words, adjectives, "ADJECTIVE", False, '"pink"')
    words = replaceall(words, names, "NAME", False, '"yellow"')
    return words

def highlight(string):
    string= string.replace(" NOUN",' <font color="red">NOUN</font>')
    string= string.replace(" VERB",' <font color="blue">VERB</font>')
    string= string.replace(" ADVERB", ' <font color="yellow">ADVERB</font>')
    string= string.replace(" ADJECTIVE", ' <font color="green">ADJECTIVE</font>')
    string= string.replace(" NAME", ' <font color="gray">NAME</font>')
    return string


string=highlight(getText('nutella.txt'))

#madlibs('nutella.txt', 'nouns.txt', 'verbs.txt', 'adjectives.txt', 'adverb.txt', 'names.txt')





print """

<html>
    <head>
        <title>Madlibs</title>
    </head>
    <body>
        <h1>Madlibs</h1>
        <p><font size="5">"""
print string
print '</font></p>'
print '<br>'
print '<br>'
print '<p><font size="15">'
print madlibs("nutella.txt", 'nouns.txt', 'verbs.txt', 'adjectives.txt', 'adverb.txt', 'names.txt')
print '</font></p>'
print '''
    </body>

</html>

'''



#Other Functions.###############
def wordreplace(word, wordlist, replace, length, change):
    if change==True:
        x=randompop(wordlist)
        if word[:length]==replace:
            return x+word[length:]
    else:
        if word[:length]==replace:
            return randompop(wordlist)+word[length:]
    
def partition(word, split):
    if split in word:
        return [word[:word.find(split)]] + [split] + [word[word.find(split) + len(split):]]
    
def join(text, lst):
    ans=""
    for each in lst:
            ans+=each+text
    return ans[:-(len(text))]
##############################


