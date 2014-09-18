#!/usr/bin/python
print 'Content-Type: text/html'
print

import random
import cgi

form = cgi.FieldStorage()
question = form.getvalue("question")

def randomsentence():
    f=open("../text/quotes.txt", 'r')
    sentences=[]
    for each in f:
        sentences.append(each[:-1])
    f.close()
    return sentences[random.randrange(len(sentences))]

print '''

<html>
    <head>
        <title>Magic 8 Ball</title>
    </head>
    <body>
        <table>
            <tr> <td><img src="../pic/8_ball_face.jpg" width='300'
            ></td> </tr> <tr>
            <td><p>'''+str(randomsentence())+"""</p></td> </tr>
        </table>
    </body>

</html>
"""
