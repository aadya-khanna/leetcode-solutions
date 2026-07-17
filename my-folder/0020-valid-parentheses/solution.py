class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        arr = list(s)
        stack = []
        
        # if not even
        if (len(arr) % 2 != 0):
            return False

        for i in arr:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        
        return True

        


        # stack: ( 
        # 
        

        
