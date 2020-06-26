class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index-1]:
                break
            index -= 1

        if index > 0:

            nums[index:] = sorted(nums[index:])
            swap_index = bisect.bisect(nums, nums[index-1], lo=index)
            nums[swap_index], nums[index-1] = nums[index-1], nums[swap_index]


        else:
            nums.reverse()
        '''

        def reverse(nums, i, j):
            while (i < j):
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j - 1
            return nums

        n = len(nums)
        index1 = -1
        for i in range(n - 2, -1, -1):  # 从后往前找第一对下降的数对num[index1+1]>nums[index1],记录索引index1
            if (nums[i] < nums[i + 1]):
                index1 = i
                break
        if (index1 == -1):  # 如果序列nums全部为降序
            nums = reverse(nums, 0, n - 1)
            return
        index2 = -1
        for j in range(n - 1, -1, -1):  # 从后往前找第一个比nums[index1]大的数的索引index2
            if (nums[j] > nums[index1]):
                index2 = j
                break
        nums[index1], nums[index2] = nums[index2], nums[index1]
        nums = reverse(nums, index1 + 1, n - 1)  # 原地反转nums中index1+1至n-1之间的序列