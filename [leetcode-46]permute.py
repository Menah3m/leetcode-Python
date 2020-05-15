'''
leetcode-46
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

'''

class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        res = []

        for index, num in enumerate(nums):
            res_nums = nums[:index] + nums[index+1:]
            for i in self.permute(res_nums):
                res.append([num] + i)
        return res


'''
使用递归解决全排列
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1: return [nums]

        self.res = []

        def helper(path, cand):
            if cand == []:
                self.res.append(path)
            for k, v in enumerate(cand):
                helper(path+[v],cand[:k]+cand[k+1:])
            
        helper([], nums)
        return self.res

'''
剑指offer-38

输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

'''
class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) <= 1:
            return list(s)
        s= list(s)
        res = []
        for index, value in enumerate(s):
            res_ = s[:index] + s[index+1:]
            for i in self.permutation(res_):
                res.append(value + i)
        return list(set(res))