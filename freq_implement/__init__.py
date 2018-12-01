import inspect
import os
from subprocess import call


path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

if call(["pyside-uic","-o",path+"/main.py",path+"/main.ui"]) is 1:
    print "Error making the python file from interface"
    exit(-1)
