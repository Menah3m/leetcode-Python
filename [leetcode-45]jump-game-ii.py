"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

来源：LeetCode-45
链接：https://leetcode-cn.com/problems/jump-game-ii

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        new_max, i_max, step = 0, 0, 0   #new_max表示每次遍历时得到的【可以到达的最远下标】  i_max表示在跳一步的范围内可以到达的最远处的下标，只有在i到达i_max时，step才会加1
        for i in range(len(nums)-1):
            num = nums[i]
            new_max = max(num+i, new_max)
            if i == i_max:
                step += 1
                i_max = new_max
                if i_max >= len(nums)-1:
                    break
        return step
