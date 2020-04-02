# Name:pivotArray
# Author:Yasu
# Time:2020/4/2

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        left_sum = sum(nums[:0])
        right_sum = sum(nums[1:])
        for i in range(len(nums) - 1):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            right_sum -= nums[i + 1]
        if left_sum == right_sum:
            return len(nums) - 1
        return -1

'''
leetcode.724
寻找中心索引
思路： 1.设置两个滑动窗口，一个装中心索引左边的和，一个装右边的和，初始值分别为 【第零个元素之前的值】，【剩余元素的和】
      2.判断两个窗口的值，若相等，则输出索引值，若不相等，则左边加上当前遍历值，右边减去当前遍历值的下一位值
'''