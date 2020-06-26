class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # 使用dp思想 dp[i][j]:以下标i为起始点，下标j为结束点的子串的最长回文子序列长度。

        n = len(s)
        if s == s[::-1]:  # 加了这个快了1000ms ...
            return n

        dp = [[0] * n for i in range(n)]
        # 注意basecase
        for i in range(n):
            dp[i][i] = 1
        # 倒着遍历 #计算dp[i][j],会用到其左边、下边和左下边信息，故倒着遍历
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]