class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # 回溯算法

        # 记录 行, 列, 正对角,负对角,不能有两个以上的棋子.

        # 如何判断是否在对角上呢?

        # 正对角就是相加之和一样的   #####

        # 负对角就是相减只差一样的   #####
        res = []  #
        s = "." * n

        def backtrack(i, tmp, col, z_diagonal, f_diagonal):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i - j not in z_diagonal and i + j not in f_diagonal:
                    backtrack(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]], col | {j}, z_diagonal | {i - j},
                              f_diagonal | {i + j})  # col | {j} 将j元素添加进col

        backtrack(0, [], set(), set(), set())
        return res