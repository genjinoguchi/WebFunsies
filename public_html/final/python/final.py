#!/usr/bin/python
print 'Content-Type: text/html'
print

import cgi, cgitb, md5
cgitb.enable()

form=cgi.FieldStorage()

def FStoD():
    d={}
    for each in form.keys():
        d[each]=form[each].value
    return d

d=FStoD()

if form.getvalue('usr')==None:
    usr=''
else:
    usr=d['usr']
if form.getvalue('pw')==None:
    pw=''
else:
    pw=d['pw']
if form.getvalue('onname')==None:
    name=''
else:
    name=d['onname']
if form.getvalue('email')==None:
    email=''
else:
    email=d['email']

usrpw=open('../files/usernames.txt','r')
usrpw=usrpw.readlines()
nusrpw=open('../files/usernames.txt','a')
good=False
reg=False
check=''

if usr != '' and pw!='' and name!='' and email!='':
    good=True
    for acc in usrpw:
        if usr not in acc.split(','):
            check+='t'
        else:
            check+='f'
    if 'f' not in check:
        reg=True
        nusrpw.write(usr+','+pw+','+name+','+email+'\n')
    

###~~~~~~~~~~~~~~~~~~~~~~~~~Good Registration~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
yhtml='<!DOCTYPE html><html><head><title>Social Network</title></head><body style="background-color: rgb(230, 230, 240)">'
if reg==True:
    yhtml+='<center><h1>Congratz! You made an account!</h1></center>'
    yhtml+='<center><form method="POST" action="../html/final.html">'
    yhtml+='<input type="submit" value="Log In!">'
    yhtml+='</form></center>'
else:
    yhtml+='<center><h1>Sorry. That username has been taken!</h1></center>'
    yhtml+='<center><form method="POST" action="../html/final.html">'
    yhtml+='<input type="submit" value="Try again!">'
    yhtml+='</form></center>'
yhtml+='</body></html>'

###~~~~~~~~~~~~~~~~~~~~~~~~~~~Bad Registration~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
bhtml='<!DOCTYPE html><html><head><title>Social Network</title></head><body style="background-color: rgb(230, 230, 240)">'
bhtml+='<center><h1>ALL FIELDS MUST BE FILLED OUT!</h1></center>'
bhtml+='<form method="POST" action="../html/register.html">'
bhtml+='<center><input type="submit" value="Try Again!"></center>'
bhtml+='</form></body></html>'

if good == True:
    print yhtml
else:
    print bhtml
