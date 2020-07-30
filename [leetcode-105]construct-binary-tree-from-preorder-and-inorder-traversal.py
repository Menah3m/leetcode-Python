"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：LeetCode-105
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        #preorder的第一个元素一定是根节点，inorder列表中根节点把左右子树一分为二
        ind = inorder.index(preorder[0]) 
        #创建根节点
        root = TreeNode(preorder[0]) 
        #递归还原左右子树
        left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        root.left = left
        root.right = right
        return root