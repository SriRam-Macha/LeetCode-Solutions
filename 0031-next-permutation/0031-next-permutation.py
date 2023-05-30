class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pivot = -1
        for i in range(len(nums)-2, -1 , -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
                
        if pivot == -1: 
            nums.reverse()
        else:
            changer = len(nums) - 1
            while changer > pivot and nums[changer] <= nums[pivot]:
                changer -= 1
            nums[pivot],nums[changer] = nums[changer] , nums[pivot]
            nums[pivot+1:] = nums[pivot+1:][::-1]