class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def length(list):
    temp = list
    counter = 1

    while temp.next is not None:
        counter += 1
        temp = temp.next

    return temp


def convert(list):

    arr = []
    curr = list

    while (curr != None):
        arr.append(curr.data)
        curr = curr.next
    return arr


def palindrom(list):
    tempArr = convert(list)
    return tempArr == tempArr[::-1]


root = Node(2)
root.next = Node(4)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(1)

print(palindrom(root))
