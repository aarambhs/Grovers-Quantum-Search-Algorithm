import qutip as qt
import numpy as np

b = qt.Bloch()

theta = np.arange(0,np.pi,0.1)

for ii in range(len(theta)):
     b.clear()
     b.add_points([np.sin(theta[ii]),0,np.cos(theta[ii])])
     b.show()
     # wait time step and load new value from file.
