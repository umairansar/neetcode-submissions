class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        lefts = ['(', '{', '[']
        rights = [')', '}', ']']
        mapping = {rights[i]:lefts[i] for i in range(len(lefts))}
        stack = []
        for c in s:
            if c in lefts:
                stack.append(c)
            elif c in rights:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != mapping[c]:
                    return False
        
        if len(stack) > 0:
            return False
        return True