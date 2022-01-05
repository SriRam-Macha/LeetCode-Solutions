class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dicc = dict()
        dito = dict()
        arr = list(s.split())
        if len(pattern) != len(arr): return False
        for i in range(len(pattern)):
            k = dicc.get(pattern[i],"")
            l = dito.get(arr[i],"")
            if k == "":
                if l =="":
                    dicc[pattern[i]] = arr[i]
                    dito[arr[i]] = pattern[i]
                else:
                    return False
            elif k != arr[i]:
                return False
            
        return True
            
                