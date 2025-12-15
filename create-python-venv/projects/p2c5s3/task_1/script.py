# Another script that has been made for you. From OpenClassrooms exercise "Manage Virtual Environments Using Requirements Files", Task 1
# Same gist: make venv, activate, try to run, fails d/t ModuleNotFound: scipy, do pip install -r requirements.txt (installs scipy), run script
# Of course there was an issue when trying to do the pip install:  NameError: name 'CCompiler' is not defined. Did you mean: 'ccompiler'?
# Researching this it may be due to the fact Python 3.12 is being used here. Updated requirements.txt to use a newer version

import scipy.special


cube_root = scipy.special.cbrt(27)
print('The cube root of 27 is {cube_root} because {cube_root} * {cube_root} * {cube_root} is 27'
      .format(**{'cube_root': cube_root}))
