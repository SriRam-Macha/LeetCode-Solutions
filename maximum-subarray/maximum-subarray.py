class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        addition = 0
        for i in range(len(nums)):
            addition += nums[i]
            if addition > maxi:
                maxi = addition
                
            if addition < 0:
                addition = 0
                
        return maxi