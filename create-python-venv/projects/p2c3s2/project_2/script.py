# Doesn't run b/c fuzzywuzzy module not installed
# After pip install fuzzywuzzy this works
from fuzzywuzzy import fuzz


ratio = fuzz.ratio('Open Classrooms', 'Openclassrooms')
print('The two strings have a similarity match of {}'.format(ratio))
