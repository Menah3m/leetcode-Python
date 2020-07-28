"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

来源：LeetCode-101
链接：https://leetcode-cn.com/problems/symmetric-tree

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirrors(lnode, rnode):
            if not lnode and not rnode:
                return True
            elif not lnode or not rnode:
                return False

            if lnode.val != rnode.val:
                return False
            return isMirrors(lnode.left, rnode.right) and isMirrors(lnode.right, rnode.left)

        return isMirrors(root, root)


# 代码2
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(L, R):
            if not L and not R:return True
            if not L or not R or L.val != R.val:return False
            return helper(L.left, R.right) and helper(L.right, R.left)
        return helper(root.left, root.right) if root else True