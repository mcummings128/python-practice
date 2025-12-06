import requests

r = requests.get('https://www.example.com')
print(r.status_code)

# Trying to run this results in '200' because we have the requests module installed and the HTTP GET was successful

#  To create an environment, use the command  python3 -m venv <environment name> .
# We will use python -m venv env in this case

# This creates an 'env' folder

# Activating the virtual environment 

# I was using Powershell, so I tried to run env/Scripts/activate.bat which didn't work--all it did was give me a new prompt
# This is because when using Powershell you have to do env/Scripts/activate.ps1 instead. A ps1 file is a plain text file that contains 1 or more Powershell commands
