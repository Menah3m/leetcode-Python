"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：剑指offer-32-ii
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []    
        while len(queue)>0:
            res = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            result.append(res)

        return result