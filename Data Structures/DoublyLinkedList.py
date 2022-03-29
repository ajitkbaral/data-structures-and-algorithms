class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Time complexity: O(1)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # Time complexity: O(1)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    # Time complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # Time complexity: O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
             self.head = None
             self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    # Time complexity: O(n)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    # Time complexity: O(n)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Time complexity: O(n)
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev= before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    # Time complexity: O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp

doubly_linked_list = DoublyLinkedList(4)
print("==========APPEND=============")
doubly_linked_list.append(5)
doubly_linked_list.append(6)
doubly_linked_list.append(7)
doubly_linked_list.append(8)
doubly_linked_list.print_list()
print("==========POP=============")
doubly_linked_list.pop()
doubly_linked_list.print_list()
print("==========PREPEND=============")
doubly_linked_list.prepend(3)
doubly_linked_list.print_list()
print("==========POP FIRST=============")
doubly_linked_list.pop_first()
doubly_linked_list.print_list()
print("==========GET=============")
print(doubly_linked_list.get(1))
print(doubly_linked_list.get(2))
print("==========SET=============")
doubly_linked_list.set_value(1, 9)
doubly_linked_list.print_list()
print("==========INSERT=============")
doubly_linked_list.insert(2, 10)
doubly_linked_list.print_list()
print("==========REMOVE=============")
doubly_linked_list.remove(2)
doubly_linked_list.print_list()