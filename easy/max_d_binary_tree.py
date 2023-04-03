# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # stack will hold the node and its depth
        stack = [(root, 1)] 
        # will update max_d while the stack has something in it
        max_d = 1

        while stack:
            # remove the last element from the stack
            node, depth = stack.pop()
            # set max depth to the max of the two 
            max_d = max(max_d, depth)

            #if there is a right node
            if node.right:
                # add it to the stack, current depth + 1 
                stack.append((node.right, depth + 1))
            #if there is a left node
            if node.left:
                # add it to the stack, current depth + 1 
                stack.append((node.left, depth + 1))
        
        return max_d