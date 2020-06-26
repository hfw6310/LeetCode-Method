class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        #
        if len(s)<=1:
            return s
        leng = len(s)
        for length in range(leng,0,-1): #length 判断的字符串长度，从leng变化到1，依次查找
            for i in range(0,leng-length+1):
                now_s=s[i:i+length]
                #print(now_s)
                if now_s==now_s[::-1]:
                    return now_s


        '''
        # 动态规划
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # 二维dp数组
        max_len = float("-inf")
        for i in range(n):  ###
            for j in range(i + 1):  ###
                if s[i] == s[j] and (i - j < 3 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j: i + 1]
                    max_len = i + 1 - j
        return res

        '''
        #把每个字母当成回文串的中心
        n = len(s)
        self.res = ""
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i -1 :
                self.res = s[i+1:j]
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        return self.res
        '''