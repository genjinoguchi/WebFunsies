#!/usr/bin/python
print "Content-type: text/html"
print

def pokemans(fil):
    stream=open(fil,'r')
    categories=stream.readline().split()
    info={}
    for each in stream:
        info[each.split(',')[0]]=each.split(',')[1:-1]
    print info

data=open('pokemon2.csv','r')
data=data.readlines()


def sumRow(rowNumber):
    string=''
    total=0
    line=data[rowNumber - 1].split(',')
    line=line[2:]
    for each in line:
        total+=int(each)
    string+='<td width="10%"><center><font color="blue">'+str(total)+'</font></center></td>'
    return string

def avrgRow(rowNumber):
    total=0
    line=data[rowNumber-1].split(',')
    line=line[2:]
    for each in line:
        total+=int(each)
    average = total * 1.0 / len(line)
    average=str(average)
    if len(average)>4:
        average=average[:4]
    string='<td width="10%"><center><font color="blue">'
    string+=average
    string+='</font></center></td></tr>'
    return string
    

def table2():
    row=2
    ans=''
    fline='<tr>'
    line=data[0].split(',')
    line=[line[1]] + ['Total'] + ['Average']
    pname='<tr><td width="10%"><center><font color="blue">'
    pname2='</font></center></td>'
    for each in line:
        fline+='<td width="10%"><center><font color="red">'+each+'</font></center></td>'
    ans+=fline + '</tr>'
    while row <= len(data):
        ans+=pname+ data[row-1].split(',')[1] + pname2 + sumRow(row) + avrgRow(row)
        row += 1
    return ans



print '''
        <html>
            <head>
                <title>Pokemon Data!</title>
                <link rel="shortcut icon" href="pokeball.jpg" type="image/x-icon" />
            </head>
            <body style="background-color:rgb(230,230,240)">
                <p> In this data set, you will be able to find the sum of all
                    the pokemon's stats and the overall average of their stats.
                    This can be extremely useful when you want to compare
                    the stats quickly with other pokemon so you can just simply
                    choose the higher numbered pokemon!
                </p>
                <p> One thing to take notice here is that there are some pokemon
                    that have different forms! Their different forms gives them
                    different statistics, so there's an actual variety of pokemon
                    with the same name.
                </p>
                <center><a href="analysis.py">You can go back to the full chart here!</a>
                </center>
                <center><table border="1" width="91%" style="background-color: rgb(230, 230, 250)">
    '''
print table2()

print '''
                </table></center>
                <embed height="2" width="0" src="pokemon3.mp3" autostart="true" loop="TRUE">
            </body>
        </html>
    '''

