class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        str1=""
        count=0
        max_count=0
        for i in range(k):
            str1+=s[i]
        for i in str1:
            if i in'aeiou':
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i-k] in 'aeiou':
                count-=1
            if s[i] in 'aeiou':
                count+=1
            max_count=max(count,max_count)
        return max_count
            
            
        