class Solution:
    # did not consider minJump of new range should be minJump away from prev range
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        n = len(s)
        print(n)

        k = 0
        rJump = 0
        lJump = 0
        while rJump < n-1:
            print(lJump, rJump)
            # find next rJump
            jump = maxJump
            while rJump + jump < n and s[rJump + jump] != '0':
                jump -= 1
                if jump < minJump:
                    return False
            rJump += jump

            # find next lJump
            jump = minJump
            while lJump + jump < n and s[lJump + jump] != '0':
                jump += 1
                if jump > maxJump:
                    return False
            lJump += jump
            print(lJump, rJump)
            
        return lJump == n-1 or (lJump + minJump < n-1)