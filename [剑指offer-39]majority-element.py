"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：剑指offer-39
链接：https://leetcode-cn.com/problems/majority-element
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        count = 0
        for num in nums:
            if count == 0:
                cur = num
            if cur == num:
                count += 1
            else:
                count -= 1
        return cur
            
        