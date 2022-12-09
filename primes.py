"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):

    for i in range (number):
        if (number % i != 0):
            return False
    return True

def get_primes(number):
    list = []
    for i in range(number):
        if(is_prime(i) == True):
            list.insert(i)
    return list



def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError('Work with Positive Numbers Only')
    else:
        # list = []
        list = get_primes(number_of_primes)
            
        return list
    
