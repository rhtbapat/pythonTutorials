import sys
import os

absFilePath = os.path.abspath(__file__)
print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)
parentDir = os.path.dirname(fileDir)
print(parentDir)

newPath = os.path.join(parentDir, 'StringFunctions')
print(newPath)

sys.path.append(newPath)

from reversestring import *

print(getName())