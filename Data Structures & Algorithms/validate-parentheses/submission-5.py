class Solution:
    def isValid(self, s: str) -> bool:
        memory = {']':'[', '}':'{',')':'('}
        stack = []

        for char in s:
            if char in memory:
                if stack and memory[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
                
            