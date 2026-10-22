class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        l=0
        max_len=0
        for i in nums:
            if i-1 not in nums:
                l=1
                while i+l in nums:
                    l+=1
                max_len=max(l,max_len)
        return max_len