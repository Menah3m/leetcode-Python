# Name:TwoNumberSums
# Author:Yasu
# Time:2020/3/18

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            x = target - nums[i]
            nums_new = nums[:]
            nums_new.remove(nums[i])
            if x in nums_new:
                return [i,nums_new.index(x)+1]

