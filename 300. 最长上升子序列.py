class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # 动态规划 时间复杂度：O(n^2),空间复杂度：O(1)
        # dp[i]表示以nums[i]结尾的最长上升子序列  !!!
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp or [0])
        '''
        #二分法
        import bisect
        arr = []
        for num in nums:
            loc = bisect.bisect_left(arr, num)
            arr[loc:loc + 1] = [num]
        # print(arr)
        return len(arr)
        '''