class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves=0
        low,high=0,len(nums)-1
        while low<=high:
            moves=moves+ abs(nums[low]-nums[high])
            high-=1
        return moves
        
        