"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：LeetCode-169
链接：https://leetcode-cn.com/problems/majority-element

"""
#摩尔投票算法
# 1.设置一个投票主选项，遍历数组，当当前值等于投票主时，count加一，否则减一，
# 2.若count变为0，则重新选举，直到最后，返回当前投票主
# 关键条件：一定有一个数超过半数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = 0, 0
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count += 1
            if n != major:
                count -= 1

        return major
            

        