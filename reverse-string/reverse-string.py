class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = len(s)
        
        for i in range(k//2):
            s[i],s[k-1-i] = s[k-1-i] , s[i]
            