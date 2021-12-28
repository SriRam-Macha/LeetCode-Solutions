class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicc = dict()
        dito = dict()
        for i in s:
            dicc[i] = dicc.get(i,0) + 1
        for j in t:
            dito[j] = dito.get(j,0) + 1
            
        if dicc == dito:
            return True
        
        return False
            