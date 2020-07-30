"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：LeetCode-113
链接：https://leetcode-cn.com/problems/path-sum-ii

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res =[]
        def helper(root, temp, sum):
            if not root:
                return []
            if not root.left and not root.right and sum==root.val:
                temp += [root.val]
                res.append(temp)
            helper(root.left, temp+[root.val], sum-root.val)
            helper(root.right, temp+[root.val], sum-root.val)
        helper(root, [], sum)
        return res