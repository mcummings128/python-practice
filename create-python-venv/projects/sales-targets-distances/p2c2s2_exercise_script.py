# In this exercise (Create your first virtual environment), someone has written this script for you. 
# You need to set up a virtual environment and run this script in it.

# To set up open Bash

# Then we will do

# python -m venv venv

# IT MIGHT TAKE A MOMENT TO SET UP THE VIRTUAL ENVIRONMENT. It took at least 60 seconds. Be patient

# Activate the virtual environment 

# source venv/bin/activate

# Then try to run this script (the file you see these comments in)

# python p2c2s2_exercise_script.py

# Get a MOduleNotFound error: geopy

# Install geopy

# pip install geopy

# Run the script again and it should be successful

# You can do a sanity check by deactivitng the virtual environment and doing 
# pip show geopy
# which probably either won't be installed or is a different version than that in the virtual environment

from geopy.distance import geodesic


potential_client_one = (51.5074, 0.1278)
potential_client_two = (40.7128, 74.0060)
print('The two clients are {} miles apart'.format(
    geodesic(potential_client_one, potential_client_two).miles))