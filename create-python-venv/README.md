
Mostly taken from the OpenClassrooms course 'Set Up a Python Environment: Create a Virtual Environment with venv' as seen here: https://openclassrooms.com/en/courses/6900846-set-up-a-python-environment/6989186-discover-python-packages

See The __Projects__ section for information about the projects (really just exercises) that are in this directory. Every section after __Projects__ is notes about virtual environments. Be sure to check the project files themselves too for additional notes and comments.

# About Virtual Environments

Use virtual environments to make sure that you have the correct packages (including specific versions of packages) available to you as part of your local development environment when you switch between projects we use virtual environments.

When you start a project you create a virtual environment. Each virtual environment contains its own Python binary and any Python packages that you choose to install inside it. The Python binary is simply the Python executable, something like python3.exe or python3 in everything not Windows. The executable is executed by the Python interpreter--if you run a command like python3 -c "print('hello')" then the python3.exe is what's being executed/run.

Each project you work on in Python should run on a virtual environment because different projects may require different versions of the same libraries. Generally, a Python installation (like the one on your local machine, or on a server) can only have one version of a package/module installed. Virtual environments help handle this by providing an isolated space for each project's dependencies, ensuring that installing or updating a package for one project does not affect other projects. If all your projects were using the same environment, installing a new/different version of a package for the needs of one project could break another project who was relying on the previous version you had installed.

# Virtual Environments and Storage in a Git repository

It is important to note that virtual environment minutiae is not typically stored in a remote Git repository because of the amount of bloat a virtual environment has associated with it. For example, in the messing around I've done the commit had 2000-something files. A lot of that is going to be packages and other things needed for the virtual enviroment to function. 

Instead of uploading all that, you could do something like put all the package versions into a requirements.txt file. This is done via the shell command

`pip freeze > requirements.txt`

That will take the output of pip freeze and throw it into the requirements.txt file. (Remember > will overwrite the contents)

__Fun fact__: Installing certain Python packages begets new shell scripts. Usually pip is installed when you install a Python version, and some magic happens with things like setup.py to let the user do shell commands like the above seamlessly

After requirements.txt has been committed to the repo, another developer could clone/fork your repo, create their own virtual environment, activate it, and then run the following command:

`pip install -r requirements.txt`

The -r flag tells pip that packages should be installed from a requirements file (requirements.txt is the standard name for it)