# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        nodes  = [[root]]
        for n in nodes:
            tmp = []
            for a in n:
                if a.left:
                    tmp.append(a.left)
                if a.right:
                    tmp.append(a.right)

            if len(tmp) != 0:
                nodes.append(tmp)

        return [[n.val for n in ll]  for ll in nodes[::-1]]
