# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''
        from collections import defaultdict

        n = len(inorder)
        #inorder_map = defaultdict(int)
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        #print(inorder_map)
        def helper(in_start, in_end, post_start, post_end):
            if in_start == in_end:
                return None
            #print(post_end)
            val = postorder[post_end - 1]
            root = TreeNode(val)
            loc = inorder_map[val]
            root.left = helper(in_start, loc, post_start, post_start + loc - in_start)
            root.right = helper(loc + 1, in_end, post_start + loc - in_start, post_end - 1)
            return root

        return helper(0, n, 0, n)
        '''
        from collections import defaultdict
        # inorder_map = defaultdict()
        inorder_map = {}
        n = len(inorder)
        for i, num in enumerate(inorder):
            inorder_map[num] = i

        def helper(in_start, in_end, post_start, post_end):
            if in_start == in_end:
                return
            val = postorder[post_end - 1]
            loc = inorder_map[val]
            root = TreeNode(val)
            root.left = helper(in_start, loc, post_start, post_start + loc - in_start)
            root.right = helper(loc + 1, in_end, post_start + loc - in_start, post_end - 1)
            # root.right = helper(loc+1, in_end, post_end-1+in_end-loc-1, post_end-1)
            return root

        return helper(0, n, 0, n)