class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            arr.append(s[i])
            i += 1
        while i < len(s) and s[i] >= "0" and s[i] <= "9":
            arr.append(s[i])
            i += 1
        if len(arr) == 0 or (len(arr) == 1 and (arr[0] == "+" or arr[0] == "-")):
            return 0

        num = 0

        for i in arr:
            if i == "-" or i == "+":
                continue

            num = num * 10 + (ord(i) - ord("0"))
        if arr[0] == "-": num = -num
        min_int=-2**31
        max_int=2**31-1
        if num > max_int:
            return max_int

        if num < min_int:
            return min_int

        return num