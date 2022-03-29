class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print values of the linked list
    def print_list (self):
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
            self.tail = new_node
        self.length += 1
        return True
    
    # Time complexity: O(n)
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp

    # Time complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # Time complexity: O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
    
    # Time complexity: O(n)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    # Time complexity: O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # Time complexity: O(n)
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


linked_list = LinkedList(4)
print("==========APPEND=============")
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.print_list()
print("==========POP=============")
linked_list.pop()
linked_list.print_list()
print("==========PREPEND=============")
linked_list.prepend(3)
linked_list.print_list()
print("==========POP FIRST=============")
linked_list.pop_first()
linked_list.print_list()
print("==========GET=============")
print(linked_list.get(1))
print("==========SET=============")
linked_list.set_value(1, 9)
linked_list.print_list()
print("==========INSERT=============")
linked_list.insert(2, 10)
linked_list.print_list()
print("==========REMOVE=============")
linked_list.remove(2)
linked_list.print_list()
print("==========REVERSE=============")
linked_list.reverse()
linked_list.print_list()