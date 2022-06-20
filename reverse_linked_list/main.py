class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_list(self, head):
        if head is None:
            return
        new_list = ListNode(head.val)
        head = head.next
        while head is not None:
            temp_node = ListNode(head.val)
            temp_node.next = new_list
            new_list = temp_node
            head = head.next
        return new_list


ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)

s = Solution()
print(s.reverse_list(ll))

