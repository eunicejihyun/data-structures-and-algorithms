# Modify your balanced string program to check whether both parentheses, (), and brackets, {}, are balanced in a string.


def balancedParenBrack(input_string: str) -> bool:
    """Checks to see if every opening parentheses has a matching closing parentheses, same with brackets.
    Open parentheses/brackets must be closed in LIFO order.

    Args:
        input_string (str): a string that may or may not contain parentheses and brackets

    Returns:
        bool: whether or not the input_string is balanced
    """
    stack = []
    matches = {"(": ")", "{": "}"}
    for char in input_string:
        if char in matches:
            stack.append(char)
        elif char in ")":
            if not stack:
                return False
            elif stack.pop() == "(":
                continue
            else:
                return False
        elif char in "}":
            if not stack:
                return False
            elif stack.pop() == "{":
                continue
            else:
                return False

    if stack:
        return False
    return True


# expected result: True
balancedString = "hello{watermelon(friend{apple}chappel)roan}"
print(balancedParenBrack(balancedString))

# expected result: False
imbalancedString = "hellowatermelon(friend{apple}chappel)roan}"
print(balancedParenBrack(imbalancedString))


# Design a max stack that allows you to push, pop, and keep track of your stack's biggest number in O(1) time.


class MaxStack:
    """ stack that also tracks the maximum value after each push by using a separate stack
    """
    def __init__(self):
        self.data = []
        self.max = []

    def push(self, element: int):
        """ Adds an item to the main stack. Compares the new element to the most recent maximum value, if the new element is larger, it is also added to the max stack. If not, the most recent maximum value is added again to the max stack.

        Args:
            element (int): new integer being added to the stack
        """
        self.data.append(element)

        max = self.peekMax()

        if not max:
            self.max.append(element)
        elif element > max:
            self.max.append(element)
        else:
            self.max.append(max)

    def pop(self) -> int:
        """ Pops the most recent item off from both the main data stack and the max stack.

        Returns:
            int: most recently added integer added to the stack
        """
        self.max.pop()
        return self.data.pop()

    def peekMax(self):
        """ Tells the user what the biggest number in the current main stack is.

        Returns:
            Returns an integer if there are items in the main stack or returns None if there are not any items in the main stack.
        """
        try:
            return self.max[-1]
        except IndexError:
            return None


stack = MaxStack()
stack.push(18)
stack.push(6)
stack.push(19)
stack.push(2)

# expected result: [18, 6, 19, 4]
print(stack.data)

# expected result: 19
print(stack.peekMax())


# expected result: 18
stack.pop()
stack.pop()
print(stack.peekMax())

