#!/usr/bin/python
print "Content-type: text/html"
print


###~~~~~~~~~~~~~~~~~~~~~~~~~~UNNECESSARY CODING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
def columns(fil):
    stream=open(fil,'r')
    columns={}
    categories=stream.readline().split(',')
    for each in categories:
        columns[each]=[categories.index(each)]
    for lines in stream:
        lines=lines[:-1].split(',')
        for each in columns:
            columns[each]+=[lines[columns[each][0]]]
    for each in columns:
        columns[each]=columns[each][1:]
    stream.close()
    return columns

def getsum(clumnname):
    return sum(map(float,(columndate[columndata[columnname]])))

def getaverage(columnname):
    return getsum(columnname)/(len(columndata[columnname]))

def getmax(columnname):
    return max(map(float,(columndata[columnname])))

def pokemans(fil):
    stream=open(fil,'r')
    categories=stream.readline().split()
    info={}
    for each in stream:
        info[each.split(',')[0]]=each.split(',')[1:-1]
    print info

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###

data=open('pokemon2.csv','r')
data=data.readlines()

def tableRow(rowNumber):
    string='<tr>'
    line=data[rowNumber - 1].split(',')
    for each in line:
        string+='<td width="10%"><center><font color="blue">'+each+'</font></center></td>'
    string+='</tr>'
    return string

def table():
    row=2
    ans=''
    fline='<tr>'
    line=data[0].split(',')
    for each in line:
        fline+='<td width="10%"><center><font color="red">'+each+'</font></center></td>'
    ans+=fline
    while row <= len(data):
        ans+=tableRow(row)
        row += 1
    return ans

columndata=columns('pokemon2.csv')


print '''
        <html>
            <head>
                <title>Pokemon Data!</title>
                <link rel="shortcut icon" href="pokeball.jpg" type="image/x-icon" />
            </head>
            <body style="background-color: rgb(230,230,240)">
                <p> In this data set, you will be able to find each and every single
                    pokemon created. You will be able to access their stats, allowing
                    you to compare pokemon with each other.<br>
                    We selected this data to be able to give stats that the majority
                    of Stuy students will care about or know about. The most
                    important thing anyone who looks through this data is the basics
                    of pokemon.
                </p>
                <center><a href="pokemon2.csv">The csv file!</a></center>
                <center><a href="http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats">Where we got the info!</a></center>
                <center><a href="analysis2.py">Sum and Averages!</a></center>
                <center><table border="1" width="91%" style="background-color: rgb(230, 230, 250)">
    '''
print table()

print '''
                </table></center>
                <embed height="2" width="0" src="pokemon.mp3" autostart="true" loop="TRUE">
            </body>
        </html>
    '''
