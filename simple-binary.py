# file name: simple-binary.py
# author: Chris McTernan
#
# Creates a binary tree node that sorts data into a recursive and iterative binary tree
# and traverses the tree using several methods

# create binary search tree as a class
class BinarySearchTree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    # defines function for printing tree in-order (left, root, right)
    def print_inorder(self) -> None:
        if self.left is not None:
            self.left.print_inorder()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.print_inorder()

    def print_preorder(self) -> None:
        print(self.data, end=' ')
        if self.left is not None:
            self.left.print_preorder()
        if self.right is not None:
            self.right.print_preorder()

    def print_postorder(self) -> None:
        if self.left is not None:
            self.left.print_postorder()
        if self.right is not None:
            self.right.print_postorder()
        print(self.data, end=' ')


# creates BST that uses recursive method
class RecursiveBinaryTree(BinarySearchTree):
    # defines function that returns true or false based on input
    def high_low(self, value: int) -> bool:
        if value < self.data:
            return False
        elif value > self.data:
            return True

    # defines function to insert values into tree based on high/low
    def insert(self, value: int) -> None:
        # if empty, adds data to root node
        if self.data is None:
            self.data = value
        # if value returns low, then branch left
        elif not self.high_low(value):
            # adds recursive tree if value does not exist at left branch
            if self.left is None:
                self.left = RecursiveBinaryTree(data=value)
            else:
                self.left.insert(value)
        # if value returns high, then branch right
        elif self.high_low(value):
            # adds recursive tree if value does not exist at right branch
            if self.right is None:
                self.right = RecursiveBinaryTree(data=value)
            else:
                self.right.insert(value)


class IterativeBinaryTree(BinarySearchTree):
    # defines function that returns true or false based on input
    def high_low(self, value: int) -> bool:
        if value < self.data:
            return False
        if value > self.data:
            return True

    # defines a function that inserts value using iterative function
    def insert(self, value: int) -> None:
        curr = None
        # stores parent node pointer
        parent = None
        # if empty, adds data to root node
        if self.data is None:
            self.data = value
        else:
            curr = self
        # iterates until current object branch is None
        while curr:
            # updates parent node pointer
            parent = curr
            # goes to left branch if value returns low, or goes to right branch if high
            if not curr.high_low(value):
                curr = curr.left
            elif curr.high_low(value):
                curr = curr.right
        # constructs node and assigns it to parent pointer
        if parent:
            if not parent.high_low(value):
                parent.left = IterativeBinaryTree(value)
            elif parent.high_low(value):
                parent.right = IterativeBinaryTree(value)


if __name__ == '__main__':
    # Initialize variables
    data_array = [8, 2, 4, 9, 5, 10, 11, 3, 6, 16, 12]
    # setup and print Binary search tree using recursive method
    # initialize recursive BST node
    recur_node = RecursiveBinaryTree(data=None)
    for i in data_array:
        recur_node.insert(i)
    print("Recursive tree in-order is:")
    recur_node.print_inorder()
    print('\n')
    print("Recursive tree pre-order is:")
    recur_node.print_preorder()
    print('\n')
    print("Recursive tree post-order is:")
    recur_node.print_postorder()
    print('\n')
    # setup and print Binary search tree using iterative method
    # initialize iterative BST node
    iter_node = IterativeBinaryTree(data=None)
    for i in data_array:
        iter_node.insert(i)
    print("Iterative tree in-order is:")
    iter_node.print_inorder()
    print('\n')
    print("Iterative tree pre-order is:")
    iter_node.print_preorder()
    print('\n')
    print("Iterative tree post-order is:")
    iter_node.print_postorder()
    print('\n')
