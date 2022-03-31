class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


hash_table = HashTable()
print("==================SET ITEM=================")
hash_table.set_item('bolts', 1400)
hash_table.set_item('washers', 50)
hash_table.set_item('lumber', 70)
hash_table.print_table()
print("==================GET ITEM=================")
print(hash_table.get_item('bolts'))
print(hash_table.get_item('washers'))
print(hash_table.get_item('lumberrss'))
print("==================ALL KEYS=================")
print(hash_table.keys())

print("\n")
print("==================INTERVIEW QUESTION FOR HASH TABLE OR DICTIONARY=================")

print('Interview question for efficient checking of an item if it exists in two different lists')
print("\n")
print('Example: List 1 = [3,4,5]; List 2 = [6,7,5], since 5 exists in both the list, it should return True')
print("\n")
print('Q. Create a function which will return True if an item exists in both the list and if not, return False')
print("\n")

print('Inefficient way: Time Complexisty = O(n^2)')
def inefficient_compare_list(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(inefficient_compare_list([3,4,5], [6,7,5]))

print("\n")

print('Efficient Way: Time Complexisty = O(2n) => O(n)')
def efficient_compare_list(list1, list2):
    my_dist = {}
    for i in list1:
        my_dist[i] = True

    for j in list2:
        if j in my_dist:
            return True
    return False

print(efficient_compare_list([3,4,5], [6,7,5]))