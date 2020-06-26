# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        # 迭代
        from collections import deque
        if not root:
            return []
        queue = deque()
        queue.append(root)
        # print(queue)
        res = []
        while queue:
            tmp = []
            n = len(queue)  # ！！！
            # print(n)
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                # print(node.val)
                if node.left:
                    queue.append(node.left)  # queue.append() 从右边加入，queue.appendleft()从左边加入
                    # queue.pop()从右边弹出，queue.popleft()从左边弹出
                if node.right:
                    queue.append(node.right)
                # print(tmp)
            res.insert(0, tmp)
        return res