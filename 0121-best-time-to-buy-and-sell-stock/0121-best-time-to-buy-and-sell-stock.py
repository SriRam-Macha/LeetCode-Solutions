class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 100000
        maxprof = 0
        
        for i in prices:
            mini = min(mini,i)
            maxprof = max(maxprof,i-mini)
            
        return maxprof
        