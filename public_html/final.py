#!/usr/bin/python
print "Content-Type: text/html"
print

import cgi, cgitb
cgitb.enable

form=cgi.FieldStorage()
usr= form.getvalue("usr")
pw= form.getvalue("pw")


info={"Edison Shi":"angelasohawtone", "Genji Noguchi": "poop"}



print """
<html>
<head>
<title>Social Network></title>
</head>

<body>





</body>
</html>
