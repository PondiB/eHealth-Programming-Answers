#-------------------------------------------------------------------------------
# Name:        Array Compaction
# Author:      Brian Pondi
#Email:        pondibrian@gmail.com
# Created:     16/01/2017
#-------------------------------------------------------------------------------
'''
QUESTION 3
Write a function that takes as input a sorted array and modifies the array to
compact it, removing duplicates..
'''
def Array_Compact(list1):
    if isinstance(list1,list):#Checking if the input is list/Array
        list2 = set(list1)#Use set to emove duplicates
        transformed_list = list(list2)#convert set back to list/Array
        return transformed_list
    else:
        print("Rerun the code and Enter a list/Array")


