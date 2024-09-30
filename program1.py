class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in paren_map:
                top_element = stack.pop() if stack else '#'
                if paren_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack







    



  

