class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c=10
        while n>=c:
            n-=c
            c-=1
        return c%2==1