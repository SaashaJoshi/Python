# This function returns a list of all those numbers in the interval [a, b) 
#  whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

from math import sqrt

def not_primes(a, b):
    final=[]
    for i in range(a,b):
        for j in range(2, int(sqrt(i)) + 1):
            if i %j  == 0:
                for x in str(i):
                    if x not in '2357':
                        break
                else:
                    final.append(i)
                break
    return final
