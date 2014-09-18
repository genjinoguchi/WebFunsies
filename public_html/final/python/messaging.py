#!/usr/bin/python
print "Content-Type: text/html"
print

import cgi, cgitb, os
cgitb.enable()

form=cgi.FieldStorage()
message=form.getvalue("message")
usr=form.getvalue("usr")
chatpartner=form.getvalue("chatpartner")
line=""
other=""
linename= ""

def combinenames(name1, name2):
    printout=""
    for each in name1.split()+name2.split():
        printout+=each
    return printout

def linenamefind():
    global usr
    global chatpartner
    linename1=combinenames(usr, chatpartner)
    linename2=combinenames(chatpartner, usr)
    stream=open("../files/messages.txt", "r")
    for each in stream:
        if linename1 in each:
            return linename1
        if linename2 in each:
            return linename2

def readchatline(linehead):
    stream=open("../files/messages.txt", "r")
    chatline=""
    for each in stream:
        if linehead in each:
            chatline=each[len(linehead):]
    stream.close()
    return chatline

def readother():
    stream=open("../files/messages.txt", "r")
    otherlines=""
    for each in stream:
        if linename not in each:
            otherlines+=each
    stream.close()
    return otherlines

def update():
    global linename
    stream=open("../files/messages.txt", "w")
    stream.write(linename+line+"\n"+other)
    stream.close()

def messaging():
    global usr
    global message
    global linename
    linename=linenamefind()
    global line
    line = readchatline(linename)
    global other
    other = readother()
    line = line.replace("\r", "")
    line= line.replace("\n", "")
    if message != None:
        line += "<tr><td>"+usr + ": " +str(message)+"</td></tr>"
    if message == "****clearmessages****":
        line=""
    update()

messaging()

htmlopen="<html>"
headopen="<head>"
title="<title>Chat:" + chatpartner + "</title>"
javascriptclose="""<script>
    function closeWindow() {
        window.open('','_parent','');
        window.close();
    }
</script>"""
headclose="</head>"
bodyopen="<body>"
chattitle="<h1>Chat With: " + chatpartner +  "</h1>"
chat="""
    <form method="Post" action="messaging.py">
        <input type="textbox" name="message"><br>
        <input type="submit" value="Send!"><br>
        (HINT: Type ****clearmessages**** to clear all messages.<br>
        Or, type ****closechat**** to close the chat)
        <input type="hidden" name="usr" value="""+'"'+usr+'"'+""">
        <input type="hidden" name="chatpartner" value="""+'"'+chatpartner+'"'+"""></form>"""
chatclose="""<a href="javascript:closeWindow();">Close Chat</a>"""
bodyclose="</body>"
htmlclose="</html>"

if message == "****closechat****":
    line=""
    update()
    print htmlopen, headopen, title, javascriptclose, headclose, bodyopen, chattitle, chatclose, bodyclose, htmlclose
else:
    print htmlopen, headopen, title, headclose, bodyopen, chattitle, "<table>"+line+"</table>", chat, bodyclose, htmlclose
