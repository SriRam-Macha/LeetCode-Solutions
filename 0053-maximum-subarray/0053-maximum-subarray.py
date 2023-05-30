class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxcurr = arr[0]
        maxglob = arr[0]
        
        for i in range(1,len(arr)):
            if arr[i] < maxcurr + arr[i]:
                maxcurr = maxcurr + arr[i]
            else:
                maxcurr = arr[i]
                
            if maxcurr > maxglob:
                maxglob = maxcurr
        
        return maxglob