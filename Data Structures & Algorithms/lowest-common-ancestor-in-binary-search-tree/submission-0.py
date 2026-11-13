# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Strategy:
        # 1. binary search and construct a path to both p and q
        # 2. compare nodes on the paths to find the lowest node
        path1 = []
        path2 = []

        path1 = self.binary_search(root, p, path1)
        path2 = self.binary_search(root, q, path2)

        # now paths are something like [rootnode, node1, node2, node3...]
        lca = root
        for node1, node2 in zip(path1, path2):
            if node1 == node2:
                lca = node1
            else:
                break

        return lca
        

    def binary_search(self, root, p, path):
        if not root:
            return []
        path.append(root)
        if root.val == p.val:
            return path
        if root.val < p.val:
            return self.binary_search(root.right, p, path)
        else:
            return self.binary_search(root.left, p, path)

            


        