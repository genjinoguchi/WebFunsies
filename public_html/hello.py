
def drawface():
    print "  1111111111111111111111111111"
    print "  l                          l"
    print "  l       /\        /\       l"
    print "  l      /  \      /  \      l"
    print " _l                          l_"
    print "l_                            _1"
    print "  1          1-----1         1"
    print "  l                          1"
    print "            \________/"
    print "           \__________/"

def hair1():
    print "  " + ("1" * 20)
    print "  " + "1" +(" " * 18) + "l"
def spiky():
    print "  " + ('! !' * 6)
    print "  " + "1" + (" " * 18) + "l"
def mohawk():
    print "  " + (" " * 9) + "!!"
    print "  " + (" " * 9) + "11"
    print "  " + (" " * 9) + "11"
    print "  " + (" " * 9) + "11"
    print "  " + (" " * 9) + "11"
    print "  " + (" " * 9) + "11"
    print "  " + (" " * 9) + "1111"
    print "  " + "1" + (" " * 18) + "l"
def carrots():
    print "  1      ^     ^     l"
def oo():
    print "  1      o     O     1"
def __():
    print "  1  ___         ___ 1"
def nonose():
    print " _1                  1_"
    print "1_                     1"
def dotnose():
    print " _1         o        1_"
    print "1_                     1"
def triangle():
    print " _1         ^        1_"
    print "1_                     1"
def l__l():
    print "  1      1____1      1"
def ____():
    print "   ________________  1"
def nomouth():
    print ""

import random
def randomhair():
    random.randint(1, 3) = hairnumb
    if hairnumb == 1:
        hair1()
    elif hairnumb == 2:
        spiky()
    else:
        mohawk()
def randomeye():
    random.randint(1, 3) = eyenumb
    if eyenumb ==1:
        carrots()
    elif eyenumb == 2:
        oo()
    else:
        __()
        mouthnumb = 3
        nosenumb = 1
def randomnose():
    if nosenumb == 1:
        nonose()
    elif nosenumb == 2:
        dotnose()
    else:
        triangle()
def randommouth():
    if mouthnumb == 1:
        l__l()
    elif mouthnumb == 2:
        nomouth()
    else:
        ____()
def randomface():
    mouthnumb=0
    nosenumb=0
    if mouthnumb != 3:
        random.randint(1, 3) = mouthnumb
    if nosenumb !=1:
        random.randint(1, 3) = nosenumb
    randomhair()
    randomeye()
    randomnose()
    randommouth()
