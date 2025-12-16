# Another script that has been made for you. From OpenClassrooms exercise "Manage Virtual Environments Using Requirements Files", Task 1
# Same gist: make venv, activate, try to run, fails d/t ModuleNotFound: ntlk
# BUT there's no requirements.txt file! So use this file to see what packages you need to install


import nltk
nltk.download('punkt_tab')

sentence = 'Open Classrooms is an excellent online learning provider'
tokens = nltk.word_tokenize(sentence)
print('By using NLTK tokenization on the sentence...')
print(sentence)
print('We get...')
print(tokens)
