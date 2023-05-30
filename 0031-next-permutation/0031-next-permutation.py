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
            changer = -1
            for i in range(len(nums) - 1, pivot , -1):
                if nums[i] > nums[pivot]:
                    changer = i
                    break
                    
            nums[pivot],nums[changer] = nums[changer] , nums[pivot]
            nums[pivot+1:] = nums[pivot+1:][::-1]