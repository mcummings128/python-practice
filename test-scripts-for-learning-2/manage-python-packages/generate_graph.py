# From Manage Python Packages exercise


# imports the matplotlib.pyplot module as a var 'plt'.
# matplotlib.pyplot is used to help create visualizations based on data, like charts, plots, etc.
# Run python3 -m pip install matplotlib (assuming you have Python 3 installed) to install the matplotlib module
# Running this will show a line graph where the line starts at 0 and moves up and to the right in a diagonal fashion

import matplotlib.pyplot as plt

# Try using pip list or python3 -m pip list to see all the modules currently installed for your Python verison
# Alternatively pip freeze lists all the packages installed, but not their dependencies
# pip freeze lists packages in a format that can be stored in a file (ex. requirements.txt)
# pip show <package1> <package2> will show the details for a specific package, or packages if multiple arguments are provided
plt.figure()
plt.plot([1, 2, 3, 4, 5])
plt.show()

print("Running pip show matplotlib...")
pip