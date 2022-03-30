class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
        
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

# Binay search tree example
#      47
#    /   \
#   21   76
#  / \   / \
# 18 27 52 82

bst = BinarySearchTree()
print("=======INERT=======")
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print("=======CONTAINS=======")
print(bst.contains(47))
print(bst.contains(21))
print(bst.contains(18))
print(bst.contains(42))
print(bst.contains(51))
print(bst.contains(61))
print("=======MIN VALUE NODE=======")
print(bst.min_value_node(bst.root).value)
print(bst.min_value_node(bst.root.right).value)