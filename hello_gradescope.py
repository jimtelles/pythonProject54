# Name: Jim Telles
# OSU Email: tellesj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Gradescope check
# Due Date: 7.3.23
# Description: Checking to see if I have a sufficient version of Python installed as well as a connection to the
#               gradescope assignment checker. And seeing if I can pull it from github.
import sys


def gradescope_test():
    return 42


cur_version = sys.version_info

if cur_version >= (3,7):
    print("This is an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is too low, it needs to be 3.7 or greater and this is " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')