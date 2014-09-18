#!/usr/bin/python
import cgi, cgitb, os, sys, stat
cgitb.enable()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LOG IN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
form=cgi.FieldStorage()

info=open('../files/usernames.txt','r')
info=info.readlines()

def getinfo(info,columnName):
    x=info[0].split(',').index(columnName)
    ans=[]
    for each in info[1:]:
        each=each.split(',')
        ans+=[each[x]]
    return ans

usrs=getinfo(info,'Username')
passes=getinfo(info,'Password')
nicks=getinfo(info,'Name')
emails=getinfo(info,'Email\n')

def FStoD():
    d={}
    for each in form.keys():
        d[each]=form[each].value
    return d

d=FStoD()

if form.getvalue('usr')==None:
    usr = ''
else:
    usr=d['usr']
if form.getvalue('pw')==None:
    pw=''
else:
    pw=d['pw']

log=False
name=''

if usr!='' and pw!='':
    if usr in usrs:
        pos = usrs.index(usr)
        if pw == passes[pos]:
            log = True
            name=nicks[pos]


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHAT SELECTION~~~~~~~~~~~~~~~~~~~~~~~~~###
ousrs=[] #other users
onames=[]

def ppllist(info):
    ppllist="<table><tr><td><h2>Friends:</h2></td></tr>"
    for each in info:
        if each!=usr:
            ppllist+="<tr><td>"+each+"</td></tr>"
    ppllist+="</table>"
    return ppllist

def choosechat(info):
    choose='<select name="chatpartner">'
    for each in info:
        choose+='<option name='+each+'>'+each+'</option>'
    choose +='</select><br>'
    return choose

chtml='<form method="POST" action="../python/messaging.py" target="_blank">'


for each in usrs:
    if each!=usr:
        ousrs+=[each]

for each in ousrs:
    pos=usrs.index(each)
    onames+=[nicks[pos]]

chtml+=ppllist(onames)
chtml+='<br><br>'
chtml+='<h1>Want to chat?</h1>'
chtml+=choosechat(onames)
chtml+='<input type="hidden" name="usr" value="'+name+'">'
chtml+='<input type="submit" value="Begin Chatting!"></form>'

def combinenames(name1, name2):
    printout=""
    for each in name1.split()+name2.split():
        printout+=each
    return printout

def writelines():
    for person in onames:
        linename1=combinenames(name, person)
        linename2=combinenames(person, name)
        makeline=True
        stream=open("../files/messages.txt","r")
        for each in stream:
            if linename1 in each:
                makeline=False
        stream.close()
        if makeline==True:
            stream=open("../files/messages.txt", "a")
            stream.write("\n"+combinenames(name, person))
            stream.close()
if log==True:
    writelines()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BAD LOGIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
bhtml="Content-Type: text/html\r\n\r\n"
bhtml+="<!DOCTYPE html><html><head><title>"
bhtml+="Social Network"
bhtml+='</title></head><body style="background-color: rgb(230, 230, 240)"><h1><center>'
bhtml+="Unidentified Username or Password! Please try again!"
bhtml+='<form method="POST" action="../html/final.html">'
bhtml+='<input type="submit" value="Log In! (Again)">'
bhtml+='</form>'
bhtml+='</center></h1></body></html>'
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Good Login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
yhtml="Content-Type: text/html\r\n\r\n"
yhtml+="<!DOCTYPE html><html><head><title>"
yhtml+="Social Network"
yhtml+='</title></head><body style="background-color: rgb(230, 230, 240)"><h1><center>'
yhtml+="Welcome " + name +"!"
yhtml+='</center></h1>'
yhtml+=chtml
yhtml+='<form method="POST" action="../html/final.html">'
yhtml+='<input type="submit" value="Log Out">'
yhtml+='</form></body></html>'


if log == True:
    print yhtml
else:
    print bhtml






