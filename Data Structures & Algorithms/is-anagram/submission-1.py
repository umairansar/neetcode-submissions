class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = {i: s.count(i) for i in s}
        t_ = {j: t.count(j) for j in t}
        
        if len(s_) != len(t_):
            return False
        
        for k in s_:
            if t_.get(k) != s_.get(k):
                return False

        return True  
        