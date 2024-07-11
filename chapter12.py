# Implement a queue using two stacks, but make enqueueing O(1)


class Stack:
    """Implementation of a stack data structure using python lists"""

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        try:
            return self.data.pop()
        except:
            raise Exception("No items left in stack to pop.")

    def peek(self):
        return self.data[-1]


class Queue:
    """Implementation of a queue data structure using 2 stacks"""

    def __init__(self):
        self.queue = Stack()
        self.temp = Stack()

    def enqueue(self, element):
        self.queue.push(element)

    def dequeue(self):
        """Dequeues the element that was added earliest (FIFO order) by popping all elements from the main stack and adding them to a temporary stack. It will then pop an item from the temp stack (the element that was added first) and return it. Before returning, the method will pop all items off the temp stack and push them back onto the main stack. This is being implemented in this way in order that the enqueue method is O(1)

        Returns:
            the element that was added first/earliest in the queue
        """
        while self.queue.data:
            self.temp.push(self.queue.pop())

        element = self.temp.pop()

        while self.temp.data:
            self.queue.push(self.temp.pop())

        return element

    def __str__(self):
        return f"front {self.queue.data} back"


queue = Queue()

for i in range(4):
    queue.enqueue(i)

# expected result: front [0, 1, 2, 3] back
print(queue)

queue.dequeue()

# expected result: front [1, 2, 3] back
print(queue)
