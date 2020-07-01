"""栈的实现"""


class Stack(object):
    """栈"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        """添加元素到栈顶"""
        self.stack.append(item)

    def pop(self):
        """弹出栈顶元素"""
        self.stack.pop()

    def peek(self):
        """查看栈顶元素"""
        return self.stack[-1]

    def is_empty(self):
        """判断是否为空"""
        return self.stack == []

    def size(self):
        """返回栈的元素数量"""
        return len(self.stack)


if __name__ == "__main__":
    s =Stack()

    s.push(2)
    print(s.peek())
    s.push(3)
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.peek())
    print(s.is_empty())