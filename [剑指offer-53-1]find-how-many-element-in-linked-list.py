"""
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

来源：剑指offer-53
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1           
        while l <= r:
            if nums[l] == target and nums[r] == target:
                return r-l+1
            elif nums[l] != target and nums[r] == target:
                l += 1
            elif nums[l] == target and nums[r] != target:
                r -= 1
            else:
                l += 1
                r -= 1
        return 0