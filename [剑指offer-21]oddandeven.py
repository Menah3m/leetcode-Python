"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。


链接：https://leetcode-cn.com/leetbook/read/illustrate-lcof/xzdt4i/
来源：剑指offer-21


"""
#思路1： 重新排列
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        odd, even = [], []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return odd + even


# 思路2： 双指针
# 
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] % 2 == 1:
                l += 1
                continue
            if nums[r] % 2 == 0:
                r -= 1
                continue
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums