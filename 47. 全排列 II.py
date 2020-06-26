class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        nums.sort()
        res = []
        visited = set()
        #print(visited)
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                #print(res)
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
                print(visited)
        backtrack(nums, [])
        return res
        '''
        #回溯算法 回溯算法关键在于:不合适就退回上一步,然后通过约束条件, 减少时间复杂度.
        if not nums: 
            return []
        nums.sort()
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])  
        return res