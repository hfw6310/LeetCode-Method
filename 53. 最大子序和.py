class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 思路一 动态规划 dp[i]表示以nums[i]结尾的字符子串的最大值
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(dp[i], res)
            # print(dp)
        return res

        '''
        #思路二 
        cur_sum = 0
        min_sum = 0
        res = float("-inf")
        for num in nums:
            cur_sum += num
            res = max(res, cur_sum - min_sum)
            min_sum = min(min_sum, cur_sum)
        return res
        '''
        '''
        res = float('-inf')
        pre_sum = 0
        for cur in nums:
            if cur >= 0:
                pre_sum += cur
                res = max(res,pre_sum)
            else:
                if pre_sum + cur > 0:
                    pre_sum += cur
                else:
                    res = max(res,cur)
                    pre_sum = 0

        return res
        '''
        '''
        #贪心算法：每一步都选择最佳选择。贪心算法可以在线性时间复杂度内找到数组中的最大值或最小值，以及和的最值问题。
        #在循环中不断找到当前最优的和 cur_sum。注意：cur_sum 是 nums[i] 和 sum + nums[i]中最大的值。这种做法保证了 sum 是一直是针对连续数组算和。

        lenth = len(nums)
        cur_sum=max_sum = nums[0]
        for i in range(1,lenth):
            cur_sum = max(cur_sum+nums[i], nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum
        '''
        '''
        #分治法
        n = len(nums)
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)
        '''