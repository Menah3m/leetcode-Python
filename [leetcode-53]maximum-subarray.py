
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：LeetCode-53
链接：https://leetcode-cn.com/problems/maximum-subarray

'''

# 一遍遍历
# 对于每一个数，若前面的子数组和为正，则加上前面的子数组作为新的子数组，
# 若为负则保留自身作为新的子数组；
# 每次遍历都与当前最大子数组和做比较，保留较大者。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        temp_sum = max_sum = nums[0]

        for num in nums[1:]:
            temp_sum = max(num, num + temp_sum)
            max_sum = max(max_sum, temp_sum)

        return max_sum

            
                