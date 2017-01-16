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
N= int(raw_input('Enter Number: '))
while True:
    #N= int(raw_input('Enter Number: '))
    if N < 0:
        print ("Input a Positive Integer")
        continue
        break
    else:
        def Perfect_Number(N):
            sum =0
            for x in range(1,N):
                if N % x == 0:
                    sum += x
           # return sum == N
                    print ('N is a Perfect Number')
                else:
                    print ('N is not a perfect Number')

