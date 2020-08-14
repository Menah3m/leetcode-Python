'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：LeetCode-64
链接：https://leetcode-cn.com/problems/minimum-path-sum
'''


"""
思路：分别计算每一个位置上方和右方的值，取其中的最小值和当前位置的值相加，最后返回右下角的值

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return False
        depth, length = len(grid), len(grid[0])
        for i in range(depth):
            for j in range(length):
                if i>0 and j>0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i>0:
                    grid[i][j] += grid[i-1][j]
                elif j>0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]