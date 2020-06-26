# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans, que = 1, [(1, root)]   #起始坐标为1，节点为根节点
        while que:
            ans = max(ans, que[-1][0] - que[0][0] + 1)
            tmp = []                #下一轮队列
            for i, q in que:   #坐标节点生成
                if q.left:
                    tmp.append((i * 2, q.left))
                if q.right:
                    tmp.append((i * 2 + 1, q.right))
            que = tmp
        return ans