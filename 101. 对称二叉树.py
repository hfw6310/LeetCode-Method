# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        #递归
        if not root:
            return True
        def Tree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val :
                return Tree(p.left, q.right) and Tree(p.right, q.left)
            return False
        return Tree(root.left, root.right)

        '''

        # 迭代
        if not root:
            return True

        def Tree(p, q):
            stack = [(q, p)]
            while stack:
                a, b = stack.pop()  #####
                if not a and not b:
                    continue
                if a and b and a.val == b.val:
                    stack.append((a.left, b.right))
                    stack.append((a.right, b.left))
                else:
                    return False
            return True

        return Tree(root.left, root.right)

        '''
        #层次遍历
        from collections import deque 

        fontier=deque()
        if not root:
            return True
        fontier.append(root)
        while fontier: 
            if len(set(fontier)) == 1 and fontier[0] == "#" :
                break
            bfs_nums=[]
            for _ in range(len(fontier)):
                head = fontier.popleft()
                if head != "#":
                    bfs_nums.append(head.val)
                    fontier.append(head.left if head.left else "#")
                    fontier.append(head.right if head.right else "#")
                else:
                    bfs_nums.append("#")
                    fontier.extend(["#", "#"])     
            if bfs_nums != bfs_nums[::-1]: 
                return False
        return True
        '''