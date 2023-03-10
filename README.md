Python Pig game
==========================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A template for a Python development project.

- [Python Pig game](#python-pig-game)
  * [Get going](#get-going)
    + [Check version of Python](#check-version-of-python)
    + [Python virtual environment](#python-virtual-environment)
    + [Install the dependencies](#install-the-dependencies)
    + [Run the code](#run-the-code)
    + [Run the validators](#run-the-validators)
    + [Run the unittests](#run-the-unittests)
    + [Run parts of the testsuite](#run-parts-of-the-testsuite)
    + [Remove generated files](#remove-generated-files)
  * [Optional targets](#optional-targets)
    + [Codestyle with black](#codestyle-with-black)
  * [More targets](#more-targets)
    + [Run the game](#run-the-game)
    + [Credits](#credits)
    + [License](#license)


About the project
--------------------------
This is a school project designed to test us in our ability to write python code using object oriented programming as well as using unittesting and well as makefiles. We were given the choice of making the game dice game pig or card game war. We chose pig due to it seeming like a more interesting game to design.

This project lets you play pig both against a friend locally or against an ai through the console.

The program is made using object oriented programming in python. 

The game is ran through commands where the running of one allows the next to be ran. These commands then run methods in the game class, which instantiates and handles all the objects in the game. The games ai opponent is handled by the intelligence class. The class works by recieving the previous rolls of the current turn along with both players total points as well as the difficulty chosen by the player. Based on this it will either chose to roll the dice or hold. The chosen difficulty decides what strategy the ai will adopt, where the higher the difficulty the closer to the optimal strategy the computer will play.


Install and play the game
--------------------------
This is how you install the game and play it if you don't intend on further developing it

### Open bash terimal
Start by opening a bash terminal in the root of the project

### Installation
Run the following commands in your bash terminal
```
# Create virtual environment
make venv
```
Wait for the venv to install, after it is done, activate it
```
# Activate virtual environment (Windwos)
. .venv/Scripts/activate
# Activate virtual environment (Linux/Mac)
. .venv/bin/activate
```
```
# Install dependencies
make install
```

### Start the game
Run the following command in your bash terminal to start the game
```
# Start the game
make run-game
```


Get going
--------------------------

This is how you can work with the development environment.



### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

The program can be started like this.

```
# Execute the main program
python pig/main.py
```

All code is stored below the directory `Sustainable-Programming-Exam-2/pig`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `pig/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest discover -s pig -p 'test_game.py'
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



Optional targets
--------------------------

These targets might be helpful when running your project.



### Codestyle with black

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).



More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.


### Credits
Makers:
Gabriel Thiman 
Github: https://github.com/GheTee

Anton Bryhagen 
Github: https://github.com/antonbryhagen

