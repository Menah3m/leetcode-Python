
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

来源：LeetCode-15
链接：https://leetcode-cn.com/problems/3sum

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>=1 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            temp = set()
            for j in range(i+1, len(nums)):
                if nums[j] in temp:
                    if len(res)==0 or res[-1]!=[nums[i], target-nums[j], nums[j]]:
                        res.append([nums[i], target-nums[j], nums[j]])
                temp.add(target-nums[j])
        return res