class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        odd, even = [], []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return odd + even