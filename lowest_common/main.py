class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def low(self, p, q):
        curr_lowest = self.val

        if p > curr_lowest and q > curr_lowest:
            return self.lowestCommonAncestor(self.right, p, q)
        if p < curr_lowest and q < curr_lowest:
            return self.lowestCommonAncestor(self.left, p, q)
        else:
            return self.val


tree = TreeNode(6)
tree.right = TreeNode(8)
tree.right.right = TreeNode(9)
tree.right.left = TreeNode(7)
tree.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left = TreeNode(0)
tree.left.right.left = TreeNode(5)
tree.left.right.right = TreeNode(3)

p = 2
q = 8

print(tree.low(p, q))

