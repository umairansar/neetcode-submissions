class Solution:
    
    alphabets="abcdefghijklmnopqrstuvwxyz"
    digits="0123456789"

    def extractWord(self, s: str) -> str:
        return list(filter(lambda x: x in self.alphabets or x in self.digits, s))
    
    def isPalindrome(self, s: str) -> bool:
        word = self.extractWord(s.lower())
        for start in range(len(word)):
            end = len(word) - 1 - start
            if word[start] != word[end]:
                return False

        return True 

        