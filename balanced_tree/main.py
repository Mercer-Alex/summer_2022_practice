class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def balanced(self, root):
        if not root:
            return True

        if root.left != None and root.right != None:
            return self.isBalanced(root.left)
            return self.isBalanced(root.right)
        if root.right != None and root.left == None:
            return False
        if root.right == None and root.left != None:
            return False
        else:
            return True




tree = TreeNode(6)
tree.right = TreeNode(8)
tree.right.right = TreeNode(9)
tree.right.left = TreeNode(7)
tree.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left = TreeNode(0)
tree.left.right.left = TreeNode(5)


print(tree.balanced(tree))
