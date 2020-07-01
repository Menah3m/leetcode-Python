"""队列的实现"""

class Queue(object):
    """队列"""
    def __init__(self):
        """初始化"""
        self.items = []
    
    def is_empty(self):
        """判断是否为空"""
        return self.items == []
    
    def enqueue(self, item):
        """进队列"""
        return self.items.insert(0, item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue("你好")
    q.enqueue("beijing")
    q.enqueue("!!")
    print(q.size())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    
