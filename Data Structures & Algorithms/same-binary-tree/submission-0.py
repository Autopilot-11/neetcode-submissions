# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edge cases
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False

        # Check values
        if not p.left and not p.right:
            if not q.left and not q.right:
                if p.val == q.val:
                    return True
                else:
                    return False
            else:
                return False
        
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
