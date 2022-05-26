class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def combined_list(a, b):
    if (a is None) or (b is None):
        return






aList = Node(5)
aList.next = Node(2)

bList = Node(9)
bList.next = Node(9)


print(combined_list(a, b))
