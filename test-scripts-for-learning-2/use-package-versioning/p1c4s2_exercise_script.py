# This works right off the bat for me
# BUT it requires matplotlib 3.2.2 and numpy version 1.19.0
# Let's use pip show to see what we have
# First I tried typing python3 to enter a Python interpreter and do pip that way, and it didn't work
# This is because pip is meant to be used in the command line, not an interactive interpreter
# Doing a regular python3 pip show mathplotlib gives the version and also a license agreement or something, a ton of info
# You can do the same for numpy

# When you need a particular version of a package, you can do:
# pip install requests~=2.2 which will install the highest version available above 2.2 , but not 3.0 or higher.

# pip install requests~=2.1.0 which will install the highest version available above 2.1.0 , but not 2.2.0 or higher.

# pip install requests>2.5.0 which will install the highest version available above 2.5.0 .

# pip install “requests>2.4.0,<2.6.0” which will install the highest version available above 2.4.0 , but lower than 2.6.0 .

import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.title('Scatter Diagram')
plt.show()