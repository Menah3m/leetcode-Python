'''

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：LeetCode-136
链接：https://leetcode-cn.com/problems/single-number

'''

'''
思路：a^b^a=b
使用异或，可以将不重复项筛出

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(1,len(nums)):
            res = res ^ nums[i]
            
        return res