class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0: return 0
        
        dicc = dict()
        start_indx = 0
        i = 0
        maxi = 0
        current = 0
        while i < len(s):
            if dicc.get(s[i],0) == 1:
                if current > maxi:
                    maxi = current
                dicc[s[start_indx]] = dicc.get(s[start_indx]) - 1
                start_indx+=1
                current -= 1
            else:
                dicc[s[i]] = 1
                current+=1
                i+=1
                
        if current > maxi : return current
                
        return maxi