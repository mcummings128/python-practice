# Another script that has been made for you. From OpenClassrooms exercise "Manage Virtual Environments Using Requirements Files", Task 1
# Same gist: make venv, activate, try to run, fails d/t ModuleNotFound: ntlk
# BUT at the moment you get this task_2.zip, there was no requirements.txt file! So use this file to see what packages you need to install
# Now that you know the package needed, let's make a requirements.txt for others who want to leverage this code by:
# Note below instructions assume you're in the task_2 folder
# 1. touch requirements.txt
# 2. source venv/bin/activate
# 3. pip freeze > requirements.txt
# 4. cat requirements.txt (This makes sure what you expect is in there)
# 5. You'll actually notice at this point there's nothing there--this is because of the way nltk.download works (assuming so anyways)
# 6. So since you didn't write anything to requirements.txt, you can probably delete it for the moment to avoid confusion. Maybe make a README.md instead if needed.
import nltk
nltk.download('punkt_tab')

sentence = 'Open Classrooms is an excellent online learning provider'
tokens = nltk.word_tokenize(sentence)
print('By using NLTK tokenization on the sentence...')
print(sentence)
print('We get...')
print(tokens)
