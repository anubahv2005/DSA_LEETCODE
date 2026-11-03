class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        move=0
        maxx=max(nums)
        for i in nums:
            j=i
            while j!=maxx:
                j+=1
                move+=1
        return move
