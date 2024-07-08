# Research and write another way to find prime numbers.

from math import sqrt

def isPrime(number: int, checkFactor: int) -> bool:
    """Recursive function that determines whether or not an int (number) is prime.
    This was an attempt to write elegant, concise code. 
    I recognize that the code is inefficient as it does not stop as soon as it finds a factor and rather checks all the integers less than the int, checkFactor.

    Args:
        number (int): the integer that is being checked for its primeness
        checkFactor (int): a potential factor of number, initially set to the square root of the number being checked plus one
        
    Raises:
        Exception: In the event that the user is checking the primeness of a number less than or equal to 1, an exception will be raised.

    Returns:
        bool: says whether or not the number being checked is prime
    """
    if number <= 1:
        raise Exception('Check a number that is greater than 1.')
    # base case
    if checkFactor == 1:
        return True
    return number % checkFactor != 0 and isPrime(number, checkFactor - 1)


# expected result: False
print(isPrime(15, int(sqrt(5))+1))

# expected result: True
print(isPrime(23, int(sqrt(5))+1))

