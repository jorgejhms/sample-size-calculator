# -- coding: utf-8 --
## sample-size-calculator

## Originally developed by Jorge Meneses (jorgejhms[at]gmail[dot]com).
## Released under a GNU General Public Licence v. 3.0.
## Versión: 0.2

import argparse

###Function definition###
        
def p_sample(N, p, z, E):
	"Sample size calculation"
	global n
	q = 1 - p
	z2 = z*z
	E2 = E*E
	n = (z2*N*p*q)/(N*E2+z2*p*q)
	return n

###Arguments definition###
parser = argparse.ArgumentParser(prog="Sample size calculator", description="Calcule the appropiate size for a sample.")
parser.add_argument("Universe", default=0, type=int, help="Size of the Universe to sample")
parser.add_argument("Error", default=0, type=float, help="Error margin desired")
parser.add_argument("Confidence", default=0, type=int, help="Confidence degree desired")
parser.add_argument("Proportion", nargs="?", default=0.5, type=float, help="Proportion desired. By default is 0.5")
parser.add_argument('--version', action='version', version='%(prog)s 0.2')
args = parser.parse_args()

	
###Variable declaration###
N = args.Universe
n = 0
p = args.Proportion
E = args.Error
z = args.Confidence
	
p_sample(N, p, z, E)

###Data presentation###
print "Universe is %r" % N
print "Proportion is %r" % p
print "Error margin is %r" % E
print "Confidence degree is %r" % z
print "Sample size is %r" % n
