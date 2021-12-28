class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicc = dict()
        for i in s:
            dicc[i] = dicc.get(i,0) + 1
        for i,j in enumerate(s):
            if dicc.get(j) == 1:
                return i
            
        return -1