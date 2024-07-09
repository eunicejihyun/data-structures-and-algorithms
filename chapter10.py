# Lines 6 - 29 are starter code


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data, next=None):
        if not self.head:
            self.head = Node(data, next)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, next)

    def __str__(self):
        linkedList = ""
        node = self.head
        while node is not None:
            linkedList += str(node.data) + " -> "
            node = node.next
        return linkedList

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while slow and fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return False

            if slow == fast:
                return True

        return False


# Create a linked list that holds the numbers from 1 to 100. Then, print every node in your list.

newLinkedList = LinkedList()
for i in range(1, 101):
    newLinkedList.append(i)
print(newLinkedList)


# Create two linked lists: one that contains a cycle and one that doesn't. Make sure each one has a `detect_cycle` method to see if it has a cycle. Call `detect_cycle` on each list.

circularLinkedList = LinkedList()
for i in range(10):
    circularLinkedList.append(i)
circularLinkedList.append(10, circularLinkedList.head)
# expected result: True
print("Is this a circular linked list?", circularLinkedList.detect_cycle())


notCircularLinkedList = LinkedList()
for i in range(13):
    notCircularLinkedList.append(i)
# expected result: False
print("Is this a circular linked list?", notCircularLinkedList.detect_cycle())
