"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：LeetCode-283
链接：https://leetcode-cn.com/problems/move-zeroes

"""

# 思路：快慢指针  快指针用来遍历每个数， 慢指针用来指定0的位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None:
            return None
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
        return 