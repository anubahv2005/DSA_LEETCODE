class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            a,b=nums[i],nums[i]
            for j in range(i,len(nums)):
                a=min(a,nums[j])
                b=max(b,nums[j])
                c+=b-a
        return c