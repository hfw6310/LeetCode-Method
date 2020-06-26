class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或 二进制按位异或
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res

        # 哈希表