"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    temp = 1
    while(temp != number):
        if (number % temp == 0 and temp != 1 or temp!= number):
            return False
        temp+=1
    return True

def get_primes(number):

    list = []
    i = 1

    while(True):
    # for i in range(number):
        if(len(list) == number):
            break
        if(i == 1):
            i+=1
        elif(is_prime(i) == True):
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
    
