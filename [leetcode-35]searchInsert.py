'''
leetcode-35
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)

        left, right, res = 0, len(nums)-1, -1

        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] >= target:
                right = mid -1
                res = mid 
            else:
                left = mid + 1
        return res



# 代码2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l