class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        for i in nums:
            x=str(i)
            arr.append(x)
        ans=[]
        for i in range(0,len(arr),2):
            ans.append(arr[i]+arr[i+1])
        out=[]
        for i in ans:
            y=int(i)
            out.append(y)
        return min(out)