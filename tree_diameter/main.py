class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    root.diameter = 0

    def tree_depth(treeNode):
        if not treeNode:
            return 0
        left = tree_depth(treeNode.left)
        right = tree_depth(treeNode.right)
        root.diameter = max(root.diameter, left + right)
        return 1 + max(left, right)

    tree_depth(root)
    return tree_depth(root)


treeRoot = TreeNode(1)
treeRoot.left = TreeNode(2)
treeRoot.left.left = TreeNode(4)
treeRoot.left.right = TreeNode(5)
treeRoot.right = TreeNode(3)

print(diameter_of_binary_tree(treeRoot))

