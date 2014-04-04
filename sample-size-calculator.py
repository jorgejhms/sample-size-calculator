## sample-size-calculator

## Originally developed by Jorge Meneses (jorgejhms[at]gmail[dot]com).
## Released under a GNU General Public Licence v. 3.0.
## Versión: 0.3

import argparse

###Function definition###
        
def p_sample(N, p, z, E):
	"Sample size calculation using proportion"
	n = 0
	q = 1 - p
	D = (E ** 2)/(z ** 2)
	n = (N*p*q)/((N-1)*D+p*q)
	print ("Universe is", N)
	print ("Proportion is", p)
	print ("Error margin is", E)
	print ("Confidence degree is", z)
	print ("Sample size is", n)

def m_sample(N, m, v, z, E):
	"Sample size calculation using mean"
	n = 0
	D = (E ** 2)/(z ** 2)
	n = (N*v)/((N-1)*D+v)
	print ("Universe is", N)
	print ("Proportion is", p)
	print ("Error margin is", E)
	print ("Confidence degree is", z)
	print ("Sample size is", n)
	
###Arguments definition###
parser = argparse.ArgumentParser(prog="Sample size calculator", description="Calcule the appropiate size for a sample.")
parser.add_argument("Type", default='mean', help="Write the type of calculation you want: 'mean' for mean sample or 'prop' for proportion sample (mean is default)")
parser.add_argument("Universe", default=0, type=float, help="Size of the Universe to sample")
parser.add_argument("Error", default=0, type=float, help="Error margin desired")
parser.add_argument("Confidence", default=0, type=int, help="Confidence degree desired")
parser.add_argument("Proportion", nargs="?", default=0.5, type=float, help="Proportion desired. By default is 0.5")
parser.add_argument("Variance", type=float, help="Variance desired")
parser.add_argument("Mean", type=float, help="Mean desired")
parser.add_argument('--version', action='version', version='%(prog)s 0.3')
args = parser.parse_args()

	
###Variable declaration###
N = args.Universe
p = args.Proportion
E = args.Error
z = args.Confidence
v = args.Variance
m = args.Mean
	
if args.Type == 'mean':
	m_sample(N, m, v, z, E);
elif args.Type == 'prop':
	p_sample(N, p, z, E)
else:
	print ("You have to chose a type of calculation")
	
