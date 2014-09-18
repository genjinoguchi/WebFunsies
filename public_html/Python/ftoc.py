#convert degrees to celcius

#f = input ("Degrees in Fahrenheit:  ")

#def ftoc(deg):
#    print (f - 32.) * 5. / 9.

def quadroots (r1, r2, r3):

    print "Larger Root:"
    print (-r2 + (((r2 ** 2.)-(4. * r1 * r3))** (1./2.)) / (2 * r1))
    print "Lesser Root:"
    print (-r2 - ((r2 ** 2.)-(4. * r1 * r3)) ** (1./2.)) / (2 * r1)

def FindQuadraticFactors():
    print "Input the coefficients to your equation"
    a =input ("X^2 Coefficient: ")
    b =input ("X Coefficient: ")
    c =input ("X^0 Coefficient: ")
    quadroots(a, b, c)

FindQuadraticFactors()
