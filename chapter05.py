# Use a list comprehension to return a list of all the words in the following list that have more than four characters: 

sampleList = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]

def minCharWords(inputList: list, n: int) -> list:
    """filter a list of words to only include words that contain more than the number of characters, n

    Args:
        inputList (list): a list of words
        n (int): a word must have more than n characters to stay in the list

    Raises:
        Exception: In the event that the user sets n to an int less than 1, an exception will be raised.

    Returns:
        list: a filtered list containing only words that contain more than n characters
    """
    if n < 1:
        raise Exception('A word needs to have at least 1 character.')
    return [word for word in inputList if len(word) > n]
     


# expected result: Exception raised
print(minCharWords(sampleList, 0))

# expected result: ['selftaught', 'programming', 'dinner', 'coding']
print(minCharWords(sampleList, 4))

