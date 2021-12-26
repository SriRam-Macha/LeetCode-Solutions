import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c = math.ceil(len(b)/len(a))
        d = a*c
        if b in d:
            return c
        else:
            d = d+a
            if b in d:
                return c+1
                
        return -1