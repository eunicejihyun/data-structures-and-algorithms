# Print the numbers from 1 to 10 recursively.

def printUpTo(n: int):
    """ print all numbers from 1 to the inputted integer in order from smallest to largest using a recursive function

    Args:
        n (int): a number greater than 1
    """
    # ensure that the int n is greater than 1
    if n < 1: 
        raise Exception('Please input a number greater than 1 into the function printUpTo')
    
    # base case
    if n == 1:
        print(1)
        return
    printUpTo(n-1)
    print(n)
    

# expected result: Exception raised
printUpTo(-3)

# function call for solution
printUpTo(10)
