# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.nodeapp(root)
    
    def nodeapp(self, node):
        if node.val == 0:
            return False
        elif node.val == 1:
            return True
        elif node.val == 2:
            return self.nodeapp(node.left) or self.nodeapp(node.right)
        else:
            return self.nodeapp(node.left) and self.nodeapp(node.right)