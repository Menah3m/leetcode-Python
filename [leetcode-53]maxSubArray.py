class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        res = sums
        for i in range(1, len(nums)):
            if sums < 0:
                sums = nums[i]
            else:
                sums += nums[i]
            res = max(res, sums)
        return res