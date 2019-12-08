class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = []
        for char in s:
            if char == '(':
                closed_brackets.append(')')
            elif char == '[':
                closed_brackets.append(']')
            elif char == '{':
                closed_brackets.append('}')
            elif char == ')' or char == ']' or char == '}':
                if len(closed_brackets) <= 0:
                    return False
                if char == closed_brackets.pop():
                    continue
                else:
                    return False
        return len(closed_brackets) == 0
