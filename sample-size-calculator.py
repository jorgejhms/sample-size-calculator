# -- coding: utf-8 --
## sample-size-calculator

## Calcule the apropiate size for a sample.

## Originally developed by Jorge Meneses (jorgejhms[at]gmail[dot]com).
## Released under a GNU General Public Licence v. 3.0.
## Versión: 0.1.1



###Funtion definition###
def sample(N, p, q, z2, E2):
    "Sample size calculation"
    n = (z2*N*p*q)/(N*E2+z2*p*q)
    return n
    
def univers():
    "Get input for Universe size"
    N = raw_input("\nUnivers size?\n> " )
    return int (N)

def proportion():
    "Get input for proportion"
    proportion = raw_input("\nProportion?\n(if doubt press ENTER)\n> ")
    if proportion == "": 
        p = 0.5 #max proportion value
    else:
        p = proportion
    return float (p)

def error():
    "Get input for error margin"
    E = raw_input("\nError margin?\n(Should not be high than 0.05)\n> ")
    if float (E) > 0.05: #Check if error margin is correct
        print "\nYou chose an error margin high than expected. Are you sure?"
        answer = raw_input("Y/N? > ")
        if answer == "N":
            return error() #return allows to restart funtion
        elif answer == "Y":
            return float (E)
        else:
            print "\nDon't understan your answer"
            print "\n...Asking again"
            return error()
    else:
        return float (E)
    
def confidence ():
    "Get input for confidence degree"
    z = raw_input("\nConfidence degree?\n(write 3 for 99.73% confidence degree and 2 for 95,45%)\n> ")
    if int (z) != 3 and int (z) != 2:
        print "\nDon't understand.\n Write again"
        return confidence()
    else:
        return int (z)
         
###Welcome message###
print """
Welcome to the sample size calculator program.
After a few steps we are going to calcule the adecuete sample size for the universe given.
"""

###Aplicación de la formula###
N = univers()
p = proportion()
E = error()
z = confidence()
q = 1 - p
z2 = z*z
E2 = E*E
n = sample (N, p, q, z2, E2)

###Data presentation###
print """
For an Universe size %r, a proportion of %r, error margin of %r, and confidence degree of %r.
Your sample size should be %r\n""" % (N, p, E, z, n)
