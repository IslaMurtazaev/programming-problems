# Valid Parentheses https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        CLOSING_TO_OPENING = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] not in CLOSING_TO_OPENING:
                opening.append(s[i])
            elif not opening or opening.pop() != CLOSING_TO_OPENING[s[i]]:
                return False
        return len(opening) == 0
