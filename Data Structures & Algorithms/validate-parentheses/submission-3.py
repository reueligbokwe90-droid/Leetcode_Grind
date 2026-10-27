class Solution:
    def isValid(self, s: str) -> bool:
        memory = {']':'[', '}':'{',')':'('}
        stack = []

        for char in s:
            if stack and char in memory:
                if memory[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return True if not stack else False
                
            