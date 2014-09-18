#!/usr/bin/python
print 'Content-Type: text/html'
print

#Check Boxes
#Radio Buttons

import cgi, math, cgitb
cgitb.enable()

form = cgi.FieldStorage()
r=form.getvalue("radius")
d=form.getvalue("diameter")
c=form.getvalue("circumference")
a=form.getvalue("area")
fontColor=form.getvalue("fontColor")
radius="No Results!"
diameter=""
circumference=""
area=""

if r!=None:
    r=float(r)
    radius="Radius:  " + str(r) + "<br>"

if d!=None:
    diameter= 2.0 * r
    diameter= "Diameter: " + str(diameter) + "<br>"

if c!=None:
    circumference= 2 * math.pi * r
    circumference= "Circumference: " + str(circumference) + "<br>"

if a!=None:
    area= (math.pi) * r**2
    area= "Area:  " + str(area) + "<br>"

if fontColor==None:
    fontColor="black"

print """
<html>
    <head>
        <title>
            Circle Math
        </title>
        <style type="text/css">
            body {background-color: green}
            h1 {color: red}
            p"""
print"{color: " + fontColor + "}"
print """
        </style>
    </head>
    <body>
        <h1>Results</h1>
        <p>"""
print radius
print diameter
print circumference
print area
print """
        </p>
    </body>

</html>
"""
