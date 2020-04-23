class CQueue:
    '''思路：添加队尾元素：直接加入A数组
             删除队首元素：①如果B数组不为空，则直接pop出B数组的最后一个元素
                          ②如果B数组为空，A数组也为空，则此时栈为空，直接返回-1
                          ③如果B数组为空，A数组补位空，则将A数组元素倒序加入B数组
                           然后pop出B组最后一个元素即可
    '''

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
        
