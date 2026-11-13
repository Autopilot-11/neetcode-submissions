# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left)-self.height(root.right)) <= 1:
            return True
        else:
            return False

        


    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
        
        
        


        

        