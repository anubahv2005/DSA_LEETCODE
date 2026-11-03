class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves=0
        median=nums[len(nums)//2]
        for i in nums:
            moves=moves+abs(i-median)
        
        return moves
        
        