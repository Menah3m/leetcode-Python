class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        res = []

        for index, num in enumerate(nums):
            res_nums = nums[:index] + nums[index+1:]
            for i in self.permute(res_nums):
                res.append([num] + i)
        return res
