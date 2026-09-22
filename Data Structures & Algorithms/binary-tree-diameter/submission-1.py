# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
get the longest path on left and right does not work, because it is not working down form the root, we are actually computing here is the diameter

recursively run DFS -> we need to be working with HEIGHT, not depth, starting at the bottom and working up.

this is not a easy dawg if this an easy its over

how do we know which node to stop at? include root but need to search for all edges. just add up all the edges under the tree?



"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root): # returns the height
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.result




