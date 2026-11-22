# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafval(root1) == self.leafval(root2)


    def leafval(self, node):
        leaves = []
        if not node.left and not node.right:
            leaves.append(node.val)
        elif not node.right:
            leaves.extend(self.leafval(node.left))
        elif not node.left:
            leaves.extend(self.leafval(node.right))
        else:
            leaves.extend(self.leafval(node.left))
            leaves.extend(self.leafval(node.right))
        
        return leaves
        
        