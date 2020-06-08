"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

来源：LeetCode-16
链接：https://leetcode-cn.com/problems/3sum-closest

"""




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:return 0
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            if i >= 1 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            #判断极端情况：最右端两数加nums[i]仍小于target，则不用看区间内其他数，反之同理
            if nums[i] + nums[r] + nums[r-1] <= target:
                l = r-1
            if nums[i] + nums[l] + nums[l+1] >= target:
                r = l+1

            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if abs(cur - target) < abs(res - target):
                    res = cur
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return target
        return res
