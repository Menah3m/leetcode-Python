"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：LeetCode-40
链接：https://leetcode-cn.com/problems/combination-sum-ii

"""



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        self.res = []
        def recursive(idx, targ, cur):
            for i in range(idx, len(nums)):
                now = nums[i]
                if now < targ:
                    if (i == idx or nums[i-1] != now):
                        recursive(i+1, (targ-now), cur+[now])
                else:
                    if now == targ:
                        self.res.append(cur+[now])
                    break
        recursive(0, target, [])
        return self.res