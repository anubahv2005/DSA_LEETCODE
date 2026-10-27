class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(pattern)!=len(s.split()):
            return False
        d={}
        d2={}
        s1=s.split()
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=s1[i]:
                    return False
            else:
                d[pattern[i]]=s1[i]
            if s1[i] in d2:
                if d2[s1[i]] != pattern[i]:
                    return False
            else:
                d2[s1[i]]=pattern[i]
        return True
