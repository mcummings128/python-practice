# From Import Python Packages and Modules exercise

# You can use an alias to import some packages as a different name like below
import numpy as np


print(f"1.2 rounded up to the nearest int is  {np.ceil(1.2)}")
print(f"1.933 rounded up to the nearest int is  {np.ceil(1.933)}")
print(f"1.2 rounded down to the nearest int is {np.floor(1.2)}")

# Try opening the Python shell in your CLI using python or python3
# Then do 
# from numpy import *
# Now you can do things like instead of having to do numpy.ceil
# ceil(1.1) 

# You DON'T want to do this in application source code though because you may start to run into naming conflicts
# For example imagine there are two math modules: IntMath and FloatMath. If they both have an add() function you can't expect which one will work

