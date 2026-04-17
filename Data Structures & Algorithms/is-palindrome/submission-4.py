class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s = list(filter(lambda x: ord('a') <= ord(x) <= ord('z') or ord('0') <= ord(x) <= ord('9'), s))
        s = "".join(s)
        print(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True