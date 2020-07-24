"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：LeetCode-47
链接：https://leetcode-cn.com/problems/permutations-ii

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:return [[]]
        res = [[]]
        for n in nums:
            temp = []
            for r in res:
                for i in range(len(r)+1):
                    temp.append(r[:i]+[n]+r[i:])
                    if i < len(r) and r[i]==n:
                        break
            res = temp
        return res