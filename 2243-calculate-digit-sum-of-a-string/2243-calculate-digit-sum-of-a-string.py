class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s)>k:
            ans=""
            for i in range(0,len(s),k):
                x=s[i:i+k]
                summ=0
                for j in x:
                    summ+=int(j)
                ans+=str(summ)
            s= ans
        return s