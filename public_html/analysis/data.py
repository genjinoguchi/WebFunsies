#!/usr/bin/python
print 'Content-Type: text/html'
print

def pokemans(fil):
    stream=open(fil, 'r')
    categories=stream.readline().split()
    info={}
    for each in stream:
        info[each.split(',')[0]]=each.split(',')[1:-1]
    print info



pokemans('pokemon.csv')
        
