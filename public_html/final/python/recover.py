#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FORMS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
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
if form.getvalue('email')==None:
    email=''
else:
    email=d['email']
if form.getvalue('rec')==None:
    rec=''
else:
    rec=d['rec']

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FILL IN CHECK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
recover= False
radio=False
pos=0

if rec!='':
    radio=True
    if rec=='user':
        if pw!='' and email!='':
            if pw in passes:
                pos = passes.index(pw)
                if email == emails[pos][:-1]:
                    recover = True
    if rec=='pas':
        if usr!='' and email!='':
            if usr in usrs:
                pos = usrs.index(usr)
                if email == emails[pos][:-1]:
                    recover = True


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~RECOVERY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
if recover == True:
    if rec=='user':
        usr=usrs[pos]
    if rec=='pas':
        pw=passes[pos]


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~BAD RECOVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
bhtml='Content-Type: text/html\r\n\r\n'
bhtml+='<!DOCTYPE html><html><head><title>'
bhtml+='Social Network</title></head>'
bhtml+='<body style="background-color: rgb(230, 230, 240)">'
bhtml+="<center><h1>You're missing information!</h1></center>"
bhtml+='<center>Go back and fill it out again!</center>'
bhtml+='<form method="POST" action="../html/recover.html">'
bhtml+='<input type="submit" value="Go back to recover!">'
bhtml+='</form></body></html>'

###~~~~~~~~~~~~~~~~~~~~~~~NOT FILLED IN RADIO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
rhtml='Content-Type: text/html\r\n\r\n'
rhtml+='<!DOCTYPE html><html><head><title>'
rhtml+='Social Network</title></head>'
rhtml+='<body style="background-color: rgb(230, 230, 240)">'
rhtml+='<center><h1>You need to select what information you forgot!</h1></center>'
rhtml+='<center>Go back and select!</center>'
rhtml+='<form method="POST" action="../html/recover.html">'
rhtml+='<input type="submit" value="Go back and SELECT!">'
rhtml+='</form></body></html>'

###~~~~~~~~~~~~~~~~~~~~~~~~GOOD RECOVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
yhtml='Content-Type: text/html\r\n\r\n'
yhtml+='<!DOCTYPE html><html><head><title>'
yhtml+='Social Network</title></head>'
yhtml+='<body style="background-color: rgb(230, 230, 240)">'
yhtml+='<center><h1>You Successfully recovered your Information!</center></h1>'
yhtml+='Username: <b>'+usr+'</b><br>'
yhtml+='Password: <b>'+pw+'</b><br>'
yhtml+='E-mail: <b>'+email+'</b><br>'
yhtml+='<form method="POST" action="../html/final.html">'
yhtml+='<center><input type="submit" value="Log In!"></center>'
yhtml+='</form></body></html>'

if radio == False:
    print rhtml
elif recover == False:
    print bhtml
else:
    print yhtml
