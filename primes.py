"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    if number == 1:
        return True

    for i in range (number):
        if (number % i == 0 and i != 1 or i!= number):
            return False
    return True

def get_primes(number):

    list = []
    i = 0

    while(True):
    # for i in range(number):
        if(len(list) == number):
            break
        if(is_prime(i) == True):
            list.append(i)
            i+= 1

    return list



def primes(number_of_primes):
    #Get first number_of_primes primes
    if number_of_primes < 1:
        raise ValueError('Work with Positive Numbers Only')
    else:
        # list = []
        # temp = 0
        # while(len(list) != number_of_primes):
        # list.append(get_primes(number_of_primes))
            # temp += 1
            
        return get_primes(number_of_primes)
    
