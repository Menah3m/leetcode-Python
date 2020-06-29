"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：LeetCode-39
链接：https://leetcode-cn.com/problems/combination-sum

"""







class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        self.res = []
        def recursive(idx, targ, cur):
            for i in range(idx, len(nums)):
                now = nums[i]
                if now < targ:
                    recursive(i, (targ-now), cur+[now])
                else:
                    if now == targ:
                        self.res.append(cur+[now])
                    break
        recursive(0, target, [])
        return self.res
