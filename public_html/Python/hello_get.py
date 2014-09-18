#!/usr/bin/python
print 'Content-Type: text/html'
print

import cgi                      #   ^common gateway interface

form = cgi.FieldStorage()       #   create a form

first_name = form.getvalue('first_name')
middle_initial = form.getvalue('middle_initial')
last_name = form.getvalue('last_name')


if first_name==None:
    first_name=""
if middle_initial==None:
    middle_initial=""
if last_name==None:
    last_name=""

first_name=first_name.strip().title()
middle_initial=middle_initial.title() 
last_name=last_name.strip().title()
if len(middle_initial) == 1:
    middle_initial += "."


print"""
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>HELLO THERE</h1>
        <p>"""
print first_name + " " + middle_initial + " " + last_name
print """  
        </p>
    </body>

"""
