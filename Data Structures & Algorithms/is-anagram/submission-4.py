class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n**2 + m**2)
        # s_ = {i: s.count(i) for i in s}
        # t_ = {j: t.count(j) for j in t}

        # O(n + m)
        s_, t_ = {}, {}
        for k in s:
            s_[k] = 1 + s_.get(k, 0)

        for k in t:
            t_[k] = 1 + t_.get(k, 0)
        
        if len(s_) != len(t_):
            return False

        return s_ == t_
        
        # for k in s_:
        #     if t_.get(k) != s_.get(k):
        #         return False

        # return True  
        