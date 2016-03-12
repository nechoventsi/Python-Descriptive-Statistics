import numpy as np
from statfunctions import *

# NumPy module for unpacking data from a file:
M, Merr, V = np.loadtxt("Data/velocity_luminosity.txt", usecols=(1, 2, 3), unpack=True, skiprows=1)

# Input from user for type of mean:
m = raw_input("Mean type? \n 1: arritmetic \n 2: quadratic \n -1: harmonic \n")
m = int(m)

print "Generalized mean of M:", genMean(M, m)

print "Variance of M:", variance(M)

print "Covariance of M and V:", covariance(M, V)