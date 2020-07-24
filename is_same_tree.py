# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(left,right):
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if right is None and left is not None:
                return False

            if left.val != right.val:
                return False

            return dfs(left.left, right.left) and dfs(left.right, right.right)
        return dfs(p,q)

