# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # 递归
        def judge(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return judge(l.left, r.right) and judge(l.right, r.left)
            return False

        if not root:
            return True
        return judge(root.left, root.right)

        '''
        # 递归调用函数会有额外的开销，迭代求解如下
        if not root:
            return True
        stack = [root.left, root.right]  #!!!
        while stack:
            node1 , node2 = stack.pop(), stack.pop()
            if not node1 and not node2 :
                continue
            if not node1 or not node2 : 
                return False
            if node1.val != node2.val : 
                return False
            stack += [node1.left,node2.right, node1.right, node2.left]
        return True
        '''