# Given a string, remove all duplicate words. For example, given the string `"I am a self-taught programmer looking for a job as a programmer."`, your function should return `"I am a self-taught looking for a job as a."`

import re

exampleString = "I am a self-taught programmer looking for a job as a programmer."


def removeDupWords(inputString: str) -> str:
    """ remove all duplicate words from an inputted sentence ignoring punctuation

    Args:
        inputString (str): a sentence potentially containing duplicate words

    Returns:
        str: the sentence without any duplicate words
    """
    seen = {}
    sentenceList = re.findall(r"[\w']+|[.,!?;]", inputString)

    for index, word in enumerate(sentenceList):
        word = word.lower()
        if word in seen:
            sentenceList[index] = ""
            sentenceList[seen[word]] = ""
        else:
            seen[word] = index
            
    return " ".join(sentenceList)


# expected result: "I am  self taught  looking for  job as   .""
print(removeDupWords(exampleString))
