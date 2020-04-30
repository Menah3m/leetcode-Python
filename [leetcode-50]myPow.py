class Solution:
    '''
    思路：递归
    1.如果n为奇数，则pow(x,n) = x*pow(x*x,(n-1)//2)
    2.如果n为偶数，则pow(x,n) = pow(x*x,n//2)
    '''
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            return 1/self.subPow(x, n)
        return self.subPow(x, n)
    
    def subPow(self, x, n):
        if n == 0:
            return 1.0
        if n % 2 == 0:
            return self.subPow(x*x, n//2)
        else:
            return self.subPow(x*x, (n-1)//2)*x
