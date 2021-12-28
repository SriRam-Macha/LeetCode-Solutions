class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicc = dict()
        dcto = dict()
        
        for i in ransomNote:
            dicc[i] = dicc.get(i,0) + 1
            
        for j in magazine:
            dcto[j] = dcto.get(j,0) + 1
            
        for i in dicc.keys():
            if dcto.get(i,0) < dicc.get(i):
                return False
        return True