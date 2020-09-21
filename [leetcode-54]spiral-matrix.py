"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：LeetCode-54
链接：https://leetcode-cn.com/problems/spiral-matrix

"""


"""
zip() 函数用于将可迭代的对象作为参数，
将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

'*'用于解包
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = matrix[0]
        matrix = [list(x) for x in zip(*matrix[1:])][::-1]
        res += self.spiralOrder(matrix)
        return res