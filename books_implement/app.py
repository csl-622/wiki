import os
import sys

path = os.getcwd()
pathFile = "python " + path + "/__init__.py"
os.system(pathFile)
pathFile = "python " + path + "/test.py"
os.system(pathFile)

