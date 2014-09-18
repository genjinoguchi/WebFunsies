import random
def moo(s):
    final=""
    num=random.randint(0, 2**(len(s)-1))
    oneortwo=random.randint(1, 3)
    for letter in (s[0:len(s)-2]):
    	if oneortwo == 1:
    		final=final+letter
    	else:
    		final=letter+final
	if oneortwo == 1:
		final=final + s[len(s)-1]
	else:
		final=s[len(s)-1] + final
    print final
