"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000

来源：剑指offer-32
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while len(queue) > 0:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
        return res