'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：LeetCode-31
链接：https://leetcode-cn.com/problems/next-permutation

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums[:] = nums[::-1]
            return 
        for i in range(len(nums)-1)[::-1]:
            if nums[i] < nums[i+1]:
                break
        for j in range(i+1, len(nums)):
            if j == len(nums)-1 or nums[j+1] <= nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        nums[i+1:] = nums[i+1:][::-1]
        return 