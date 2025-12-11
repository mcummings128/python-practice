# Taken from exercise "Work with multiple virtual environments"

# Trying to run this on local machine may/may not result in a failure d/t ModuleNotFound error: matplotlib

# Even if it is installed, in real life your local machine isn't going to be the end all be all. Even then, global Python package installations should be kept to a minimum

# So let's make another virtual environment

# python -m venv venv

# Doing pip freeze in the activated virtual environment shows no packages

# Let's thus install matplotlib

# pip install matplotlib

# Now let's run the script

# python3 demo.py

# The script runs, yay (getting some Figure... error related to matplotlib, but that's not the point)

# Observe what happens when you switch to the demo-app directory

# cd ../demo-app

# And then try to activate the virtual environment over there (at this point you're already in the activated demo-app-2/venv virtual environment)

# source myvenv/bin/activate

# See how the context switches to the myvenv context without having to deactivate the venv virtual environment

# If you run deactivate, it won't take you back to the venv virtual environment, you go back to the regular shell

import matplotlib.pyplot as plt
plt.figure()
plt.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
plt.show()