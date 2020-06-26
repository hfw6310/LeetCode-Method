class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # 动态规划 f(i, j)就是text1[0]~text1[i]和text2[0]~text2[j]之间的最长公共子序列长度

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] != text2[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return dp[-1][-1]