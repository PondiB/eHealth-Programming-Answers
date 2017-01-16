#-------------------------------------------------------------------------------
# Name:        Array Compaction
# Author:      Brian Pondi
#Email:        pondibrian@gmail.com
# Created:     16/01/2017
#-------------------------------------------------------------------------------
'''
QUESTION 2
Implement a function with signature find_chars(string1, string2) that takes two
strings and returns a string that contains only the characters found in string1
and string2 in the order that they are found in string1.
'''
def find_chars(string1, string2):
    Similar_chars = ""
    for c in string1:
        for cc in string2:
            if c == cc:
                Similar_chars += c
                break
    return Similar_chars
