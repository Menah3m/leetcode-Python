'''
leetcode-268
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，
找出 0 .. n 中没有出现在序列中的那个数。

'''




class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)           #找到目标数组中最大值

        if len(nums) != max_:      # 判断缺失数是否为给出的序列中的最大的那个书
            return max_+1
            
        li = [x for x in range(max_+1)] #创建一个没有缺失数字的顺序序列数组

        nums.extend(li)                 #合并两个数组
# 找出数组中只出现了一次的值   leetcode-136
        res = nums[0]                    

        for i in range(1,len(nums)):
            res = res ^ nums[i]
        
        return res
