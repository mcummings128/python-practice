# Doesn't run b/c dateutil module not installed
# After pip install python-dateutil this works
# It's interesting to note that pip install dateutil doesn't work, but you can still reference dateutil in the
# On the flip side, from python-dateutil doesn't work either
# You can activate the virtual environment here, run the script, and then navigate over to project_1 and activate its venv
from dateutil import parser

# Take a string and parse into datetime object
parsed_date = parser.parse('3rd January 2014')
print('The type of the parsed date is {}'.format(type(parsed_date)))
