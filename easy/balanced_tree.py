# Balanced Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # if the root is empty, it is balanced
            if not root:
                return [True, 0]
            # set the left sub tree to dfs(root.left)
            # set the right sub tree to dfs(root.right)
            left, right = dfs(root.left), dfs(root.right)
            
            # if left and right are both returning true, AND the height of left - right is less than 1
            bal = (left[0] and right[0]
                 and abs(left[1] - right[1]) <= 1)
            
            # return [is this tree balanced, height of tree]
            return [bal, 1 + max(left[1], right[1])]
        # return the bool from dfs(root)
        return dfs(root)[0]
