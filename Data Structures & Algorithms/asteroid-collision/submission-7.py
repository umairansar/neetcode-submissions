class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            cur = asteroids[i]
            if cur < 0:
                stack.append(cur)
                while len(stack) > 1 and stack[-2] > 0:
                    this = stack.pop()
                    old = stack.pop()
                    if this + old < 0:
                        stack.append(this)
                    elif this + old > 0:
                        stack.append(old)
                        break
                    else:
                        break
            else:
                stack.append(cur)
        return stack