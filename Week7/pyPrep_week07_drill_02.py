# 
# Write a function called textCrawl, this function will take one parameter, a string of text
# and will return 0. This function will take the string it was given and have it crawl across
# the screen.
# Use the python time library to help you.
# https://docs.python.org/3/library/time.html
# 
# -------------------------------------------------------------------------------------------

import sys
import time

def textCrawl(a_string):
    for char in a_string:
        time.sleep(0.1)
        print(char, end = "")

hi = "bloody hell"

textCrawl(hi)

