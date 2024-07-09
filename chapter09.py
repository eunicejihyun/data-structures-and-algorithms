# Given an array called an_array of non-negative integers, return an array consisting of all the even elements of an_array, followed by all the odd elements of an_array

from random import randint

# randomly generated list of 50 non-negative integers ranging from 1, 100 using the randint method
an_array = [randint(1, 100) for n in range(50)]


def evenThenOdd(inputList: list) -> list:
    """ Orders the list such that all even numbers come before the odd numbers by comparing numbers at the front (head) and back (tail) of the list.

    Args:
        inputList (list): an unordered list containing integers

    Returns:
        list: an "ordered" list with even numbers coming before odd numbers
    """
    headIndex = 0 
    tailIndex = len(inputList) - 1
    
    while tailIndex > headIndex:
        head = inputList[headIndex]
        tail = inputList[tailIndex]
        headEven = head % 2 == 0
        tailEven = tail % 2 == 0
        
        if headEven and tailEven:
            # if both are even, move the tail item next to the front and skip head ahead
            next = inputList[headIndex + 1]
            inputList[headIndex + 1] = tail
            inputList[tailIndex] = next
            headIndex += 2
            continue
        elif not headEven and not tailEven:
            # if both are odd, move the head item to the back and skip tail ahead
            next = inputList[tailIndex - 1]
            inputList[tailIndex - 1] = head
            inputList[headIndex] = next
            tailIndex -= 2
            continue
        elif not headEven and tailEven:
            # switch positions if head is odd and tail is even
            inputList[tailIndex] = head
            inputList[headIndex] = tail
        
        tailIndex -= 1
        headIndex += 1
                             
    return inputList


# function call for solution
print(evenThenOdd(an_array))
    
    
    
    