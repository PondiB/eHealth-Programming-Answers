#-------------------------------------------------------------------------------
# Name:        Perfect Numbers
# Author:      Brian Pondi
#Email:        pondibrian@gmail.com
# Created:     16/01/2017
#-------------------------------------------------------------------------------
'''
QUESTION 1
Given a number N return whether N is a perfect number or not.
(A perfect number is a positive integer that is equal to the sum of its proper
positive divisors excluding the number itself)
'''
N= int(raw_input('Enter any  Number: '))#Use raw_input in python 2 and input in python 3
sum = 0
for x in range(1,N):
    if N % x ==0:
        sum += x
if sum == N:
    print("{} is a Perfect Number").format(N)
else:
    print ("{} is not a Perfect Number").format(N)

