class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # 动态规划 方法一
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[(k, n)] = ans
            return memo[(k, n)]

        return dp(K, N)
        '''
        #动态规划 方法二
        dp = list(range(N+1))
        dp2 = [0] * (N+1)
        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) >= max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2[n] = 1 + max(dp[x-1], dp2[n-x])

            dp = dp2[:]

        return dp[-1]
        '''