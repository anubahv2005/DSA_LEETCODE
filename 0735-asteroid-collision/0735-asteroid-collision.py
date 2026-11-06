class Solution(object):
    def asteroidCollision(self, n):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in range(len(n)):
            if n[i]>0:
                stack.append(n[i])
            elif n[i]<0:
                while stack and stack[-1]>0:
                    if stack[-1]>abs(n[i]):
                        break
                    elif stack[-1]<abs(n[i]):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(n[i])

        return stack