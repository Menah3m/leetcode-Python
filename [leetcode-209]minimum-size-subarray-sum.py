"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

来源：LeetCode-209
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum

"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, cur = 0, 0
        min_len = float("inf")

        for r in range(len(nums)):#增加右指针进行遍历
            cur += nums[r]        #求和
            while cur >= s:       #若此时区间内的和大于目标值则进行比较
                min_len = min(min_len, r-l+1) # 更新 区间最小长度
                cur -= nums[l]                #移动左指针，同时要将左端值从和当中去掉
                l += 1
        return min_len if min_len != float("inf") else 0