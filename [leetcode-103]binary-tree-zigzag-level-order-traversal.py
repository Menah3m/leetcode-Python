"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：LeetCode-103
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
思路： 在BFS的基础上增加一个flag，当置1时，该层结果反转，并把flag置0，否则正常添加。
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = [root], []
        flag = False
        while len(queue)>0:
            level=[]
            for i in range(len(queue)):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            if flag:
                res.append(level[::-1])
            else:
                res.append(level)
            flag = False if flag else True
        return res                   
