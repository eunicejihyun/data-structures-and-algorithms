# Lines 4 - 24 are starter code


class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree


# Write a function that can accept a binary tree as a parameter and return `True` if it is a min heap and `False` if not.


def isMinHeap(tree: BinaryTree) -> bool:
    """checks if a binary tree is a min heap by using depth-first traversal to see if any children nodes have a value less than its parent

    Args:
        tree (BinaryTree): a binary tree

    Returns:
        bool: returns True if the binary tree is a min heap and False if not
    """

    current = [tree]

    while current:
        node = current.pop()
        while node:
            if node.right_child:
                if node.key > node.right_child.key:
                    return False
                current.append(node.right_child)
            if node.left_child:
                if node.key > node.right_child.key:
                    return False
            node = node.left_child

    return True
