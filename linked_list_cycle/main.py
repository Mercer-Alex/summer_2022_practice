class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(root, index):
    try:
        slow = root
        fast = root.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

def has_cycle_dict(root):
    inList = set()
    while root:
        if root in inList:
            return True
        inList.add(root)
        root = root.next
    return False

cycle_list = ListNode(3)
cycle_list.next = ListNode(2)
cycle_list.next.next = ListNode(0)
cycle_list.next.next.next = ListNode(-4)
cycle_list.next.next.next.next = cycle_list
index = 1

print(has_cycle(cycle_list, index))

print(has_cycle_dict(cycle_list))

