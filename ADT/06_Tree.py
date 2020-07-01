"""树的ADT"""

class Node(object):
    #节点类
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self,root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有节点进行层次遍历
            while queue:
                cur = queue.pop(0)
                #弹出队列的第一个元素
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == Node:
                    cur.rchild = node
                    return 
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return 
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root)
        """递归实现中序遍历"""
        if root == None:
            return 
        self.preorder(root.lchild)
        print(root.elem)
        self.preorder(root.rchild)

    def postorder(self, root):
        """递归实现后序遍历"""
        if root == None:
            return 
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        print(root.elem)
    
    def breadth_travel(self, root):
        """利用队列实现数的层次遍历"""
        if root == None:
            return 
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
                