# Lines 4 - 54 are starter code


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

    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False

    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []
        return

    # Add a method called `has_leaf_nodes` to your binary tree code. The method should return `True` if the tree has leaf nodes and `False` if it does not.

    def has_leaf_nodes(self) -> bool:
        """checks to see if there are leaf nodes (nodes without children) in the binary tree via depth first traversal

        Returns:
            bool: True if the tree has leaf nodes, False if the tree does not have leaf nodes
        """
        current = [self]

        while current:
            node = current.pop()
            while node:
                if not (node.left_child or node.right_child):
                    return True
                if node.right_child:
                    current.append(node.right_child)
                node = node.left_child

        return False

    # Invert a binary tree using a depth-first traversal.

    def invertDepthFirst(self):
        """inverts a tree (switch left and right child at every level) via depth-first traversal

        Returns:
            nothing
        """
        current = [self]

        while current:
            node = current.pop()
            while node:
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp

                if node.right_child:
                    current.append(node.right_child)
                node = node.left_child

        return


tree = BinaryTree(0)
tree.insert_left(1)
tree.insert_right(2)
tree.insert_left(3)
tree.insert_right(4)
tree.insert_left(5)
tree.insert_right(6)

# expected result: True
print(tree.has_leaf_nodes())
