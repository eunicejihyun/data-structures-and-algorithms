# Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list.

sampleList = ['Apple', 'Blue', 'Critter', 'Dog', 'Elephant', 'Farm', 'Gray', 'Hawk', 'Igloo', 'Jaguar', 'Kite', 'Lemon', 'Map']

# ..............................
# easy way
# ..............................
from bisect import bisect_left

def easyBinSearch(listInput: list, target: str) -> bool:
    """ Use a binary search using the bisect_left function from the bisect module to find if the target str is in the listInput list

    Args:
        listInput (list): a lexiographically ordered list
        target (str): the word that we are searching for in the input list

    Returns:
        (bool): whether or not the the target str is in the listInput list
    """
    # ensure that function is not case-sensitive
    lowercaseList = [word.lower() for word in listInput]
    index = bisect_left(lowercaseList, target.lower())
    try:
        if lowercaseList[index] == target:
            print(f"'{target}' found in list")
            return True
        print(f"'{target}' not found in list")
        return False
    except IndexError:
        # not DRY but must account for possibility that index returned by bisect_left is outside of list bounds
        print(f"'{target}' not found in list")
        return False


# expected result: 'zoo' not found in list
easyBinSearch(sampleList, 'zoo')

# expected result: 'kite' found in list
easyBinSearch(sampleList, 'kite')



# ..............................
# hard way using ord function (comparing the letters of each word using their ascii value)
# ..............................

def compareWords(target: str, comparison: str):
    """ Compare two words to understand lexicographic order. This function is only used in the context of the hardBinSearch function (below).

    Args:
        target (str): the word that we are searching for in the input list (from hardBinSearch function)
        comparison (str): the word that we are comparing the target string to that we know is in the input list (from hardBinSearch function)

    Returns one of the following options as a str:
        '>': target string is lexicographically bigger than comparison string
        '<': target string is lexicographically smaller than comparison string
        '=': target string is lexicographically equal to comparison string
    """
    
    for index, letter in enumerate(target):
        try:
            if ord(letter) > ord(comparison[index]):
                return '>'
            elif ord(letter) < ord(comparison[index]):
                return '<'
        except IndexError:
            return '>'
        
    if len(target) < len(comparison):
        return '<'
    return '='
    

def hardBinSearch(listInput: list, target: str) -> bool:
    """ Use a binary search to find if the target str is in the listInput list.
    This function references the compareWords function.

    Args:
        listInput (list): a lexiographically ordered list
        target (str): the word that we are searching for in the input list

    Returns:
        (bool): whether or not the the target str is in the listInput list
    """
    # ensure that function is not case-sensitive
    lowercaseList = [word.lower() for word in listInput]
    target = target.lower()
    
    upper = len(listInput) - 1
    lower = 0
    
    while upper >= lower:
        mid = (upper + lower)//2
        result = compareWords(target, lowercaseList[mid])
        
        if result == ">":
            lower = mid + 1
            continue
        elif result == "<":
            upper = mid - 1
            continue
        else:
            print(f"'{target}' found in list")
            return True
    
    print(f"'{target}' not found in list")
    return False
        

# expected result: 'elephant' found in list
hardBinSearch(sampleList, 'elephant')

# expected result: 'apples' not found in list
hardBinSearch(sampleList, 'apples')

    



