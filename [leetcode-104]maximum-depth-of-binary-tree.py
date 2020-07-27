"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：LeetCode-104
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth, queue = 0, [root]
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            depth += 1
        return depth
                
# 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0  #终止条件
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
                