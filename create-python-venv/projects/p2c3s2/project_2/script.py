# Doesn't run b/c fuzzywuzzy module not installed
# After pip install fuzzywuzzy this works
# You can activate the virtual environment here, run the script, and then navigate over to project_1 and activate its venv
from fuzzywuzzy import fuzz


ratio = fuzz.ratio('Open Classrooms', 'Openclassrooms')
print('The two strings have a similarity match of {}'.format(ratio))
