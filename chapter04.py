# Research and write a sorting algorithm that is not a bubble sort, insertion sort, or merge sort.

from heapq import heapify, heappop
from random import randint

# randomly generated list of 50 non-negative integers ranging from 1, 100 using the randint method
numList = [randint(1, 100) for n in range(50)]


def heapSort(inputList: list) -> list:
    """uses a standard min heap using the heapq module to pull the smallest item in the list and add to a new sorted list that will be returned

    Args:
        inputList (list): unsorted list of integers

    Returns:
        list: sorted list of integers
    """
    heapify(inputList)
    sorted = []

    while inputList:
        sorted.append(heappop(inputList))

    return sorted


# function call for solution
print(heapSort(numList))
