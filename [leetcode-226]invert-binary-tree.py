"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：LeetCode-262
链接：https://leetcode-cn.com/problems/invert-binary-tree

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return root
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)    
        dfs(root)
        return root