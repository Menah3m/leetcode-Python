"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:

n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

来源：LeetCode-561
链接：https://leetcode-cn.com/problems/array-partition-i

"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums)
        nums = sorted(nums)
        l, r, res = 0, len(nums)-2, 0
        while l <= r:
            if l == r:
                res = res + nums[l]
            else:
                res = res + nums[l] + nums[r]
            l += 2
            r -= 2
        return res
            
        