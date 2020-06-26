import functools


class Solution:
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        '''
        #动态规划 自顶向下

        if s == s[::-1]:
            return 0
        ans = float("inf")
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans

        '''
        # 动态规划 自底向上 用数组min_s记录到字符串i位置需要分割次数.
        min_s = list(range(len(s)))
        # print(min_s)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    # 说明不用分割
                    if j == 0:
                        min_s[i] = 0
                    else:
                        min_s[i] = min(min_s[i], min_s[j - 1] + 1)
        return min_s[-1]