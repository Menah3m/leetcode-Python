
'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof

'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp_list = [i for i in range(nums[-1]+1)]
        if temp_list == nums:
            return nums[-1]+1
        s1 = set(temp_list)
        s2 = set(nums)
        
        r = list(s1-s2)
        res = r[-1]
        return res