from qutip import *
#modules initialised and called
import numpy as np
#numpy called as np to perform pure mathematical calculations
import math
import time

b= Bloch()
#a class which holds various bits of data regarding a 3 dimensional spherical grid
#This is stored in the named memory location b

startingvector = [1,0,0]
#choose an arbitrary state for the starting position of the qubit
b.add_vectors(startingvector)
#vector appended to the class as a directional vector



b.make_sphere()


xz = [np.sin(th) for th in np.linspace(((math.pi)/2),math.pi, 20)]
#set of x coordinates to move from start to finish in 20 steps

yz = np.zeros(20)
#as we are rotating about y, we do not need the y coordinates to move
zz = [np.cos(th) for th in np.linspace(((math.pi)/2), (math.pi), 20)]
# set of z coordinates to move from start to finish in 20 steps
vectorpoints = [xz, yz, zz]
#set of vectors are now stored on a single multidimensional array

b.add_points(vectorpoints)
#vectorpoints array is now fed into this function
#vectorpoints now added to class b




x2z = np.zeros(40)
#x coordinates now unchanged
y2z = [np.sin(th) for th in np.linspace((math.pi), 0, 40)]
#second set of y coordinates to move from the phase difference to inversion


z2z = [np.cos(th) for th in np.linspace((math.pi), 0, 40)]
#second set ofz coordinates to move from the phase difference to inversion

newvectorpoints = [x2z,y2z,z2z]
#set of vectors for inversion are now stored on a single multidimensional array

b.add_points(newvectorpoints, 'm')
#newvectorpoints array is now fed into this function
#newvectorpoints now added to class b
print (b)
#printing information about class b at this moment in time
b.show()
