# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        #自顶向下 不断递归左右子树, 有重复部分,所以时间复杂度为O(n^2)
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
	# 求高度
    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.right),self.height(node.left))
        '''
        #自底向上，时间复杂度为O(n)
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right)
        helper(root)
        return self.res