class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        #动态规划方法
        """
        状态：f(i)表示以s[i]结尾的最长有效括号
        状态转移方程：
        如果s[i]是"("，那么以它结尾的括号字符串一定是无效的，因此为f(i)=0
        如果s[i]是")"，那么分为两种情况：
        如果前一个字符s[i-1]是"("，那么只需要在f(i-2)上加2即可得到f(i)
        如果前一个字符s[i-1]是")"，那么需要看前一个字符的有效长度之前的一个字符s[i-1-dp[i-1]]是否为"("，是的话，则它们能构成一个很长的匹配，长度为dp[i-2-dp[i-1]]+dp[i-1]+2
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2   #用 dp[i] 表示以 i 结尾的最长有效括号
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        print(dp)
        return res
        '''

        # 栈
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    # print(stack[-1])
                    res = max(res, i - stack[-1])
        return res