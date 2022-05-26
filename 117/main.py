class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def min_sum(root):
    if root is None:
        return

    level_dict = {}
    queue = []
    queue.append(root)

    level = 0

    lowest = float('inf')
    lowestLevel = 0

    while(len(queue) > 0):
        count = len(queue)
        level += 1
        for x in range(count):
            level_dict[level] = level_dict.get(level, 0) + queue[0].data
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    for key, value in level_dict.items():
        if value < lowest:
            lowest = value
            lowestLevel = key

    return lowestLevel



root = Node(15)
root.left = Node(3)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(8)

print(min_sum(root))