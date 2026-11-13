# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)

    def depth(self, root):
        # edge case check
        if root == None: 
            return 0
        # base case: no more nodes
        if root.left == None and root.right == None:
            return 1
        return max(self.depth(root.left), self.depth(root.right)) + 1
        




        