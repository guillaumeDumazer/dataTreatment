#!/usr/bin/python
e
# Python version for the moving average over every column of a data file

import sys
import numpy as np

if (len(sys.argv) <= 2):
 print "Need arguments : smoothin.py DATAFILE_NOISY DATAFILE_SMOOTH";
 sys.exit();

data = np.loadtxt( str(sys.argv[1]) ); # Noisy data file

P_2 = 3; # Half-window

# Moving average operation on every columns:
dataSmooth = np.array( [ sum( data[i-P_2:i+P_2,:] ) / ( 2*P_2 ) for i in range(P_2, np.shape(data)[0]-P_2) ] );

np.savetxt( str(sys.argv[2]), dataSmooth ); # Save the smoothed data file
