class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx=max(nums)
        minn=min(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]<maxx and nums[i]>minn:
                count+=1
            else:
                continue
        return count