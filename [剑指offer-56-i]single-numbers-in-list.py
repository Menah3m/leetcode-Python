"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：剑指offer-56
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof

"""

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dic = {}
        if not nums:
            return res
        for i in nums:
            dic[i] = i in dic
        for i in nums:
            if dic[i] == False:
                res.append(i)
        return res