# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = False
        if not root or not subRoot:
            return flag
        if root.val == subRoot.val:
            flag = self.same(root, subRoot)
        flag = flag or self.isSubtree(root.left, subRoot)
        flag = flag or self.isSubtree(root.right, subRoot)
        return flag

    # Start processing if initial value equal
    def same(self, r, s):
        if not r and not s:
            return True
        if not r or not s or r.val != s.val:
            return False
        return r.val == s.val and self.same(r.left,s.left) and self.same(r.right, s.right)


        