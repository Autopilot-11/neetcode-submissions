# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.inverthelper(root)
        
    
    def inverthelper(self, root):
        # Edge case empty check
        if root == None:
            return None
        # Base case: leaf node
        if root.left == None and root.right == None:
            return root
        temp = root.left
        root.left = self.inverthelper(root.right)
        root.right = self.inverthelper(temp)
        return root

      