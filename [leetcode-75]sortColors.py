'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：LeetCode-75
链接：https://leetcode-cn.com/problems/sort-colors

'''

# 1次遍历（计数） + 1次遍历（填值）
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r_0, w_1, b_2 = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                r_0 +=1
            if nums[i] == 1:
                w_1 +=1
            if nums[i] == 2:
                b_2 +=1
        
        nums[:] = [0]*r_0 + [1]*w_1 + [2]*b_2
        return nums


# 双指针（0 2）
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, left, right = 0, 0, len(nums)-1
        while i <= right:
            
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                i -= 1
                right -= 1
            i += 1
        return nums